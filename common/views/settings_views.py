import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.conf import settings

from common.forms import ProfileForm


@login_required(login_url='common:login')
def base(request):
    """
    계정설정 기본화면
    """
    context = {'settings_type': 'base'}
    return render(request, 'common/settings/base.html', context)


# todo 프로필 전체에 대한 UPDATE 뷰로 사용? 그럼 base 프로필은 어케 처리?
def profile_modify(request):
    """
    계정설정 이미지 등록 및 변경
    """
    profile = request.user.profile
    if request.method == "POST":
        old_image = profile.image
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # 기존 이미지 파일 삭제
            if old_image and 'image' in request.FILES:
                os.remove(os.path.join(settings.MEDIA_ROOT, old_image.path))
            form.save()
            return redirect(request.path_info)
    else:
        form = ProfileForm(instance=profile)
    context = {'form': form, 'profile': profile, 'settings_type': 'image'}
    return render(request, 'common/settings/image.html', context)


def profile_image_delete(request):
    """
    계정설정 이미지 삭제
    """
    profile = request.user.profile
    # 기존 이미지 파일 삭제
    if profile.image:
        os.remove(os.path.join(settings.MEDIA_ROOT, profile.image.path))
    profile.image = None
    profile.save()
    return redirect('common:settings_image')


class PasswordChangeView(auth_views.PasswordChangeView):
    """
    비밀번호 변경
    """
    template_name = 'common/settings/password_change.html'
    success_url = reverse_lazy('index')

    # def form_valid(self, form):  # 유효성 검사 성공 이후 로직
    #     messages.success(self.request, '암호를 변경했습니다.')  # 성공 메시지
    #     return super().form_valid(form)  # 폼 검사 결과를 반환

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'settings_type': 'password',
        })
        return context
