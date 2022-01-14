from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from common.forms import UserForm


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect(request.POST.get('next', 'pybo:index'))
    else:
        form = UserForm()
        next = request.GET.get('next', '')
    return render(request, 'common/signup.html', {'form': form, 'next': next})


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'common/password_change.html'
    success_url = reverse_lazy('index')

    # def form_valid(self, form):  # 유효성 검사 성공 이후 로직
    #     messages.success(self.request, '암호를 변경했습니다.')  # 성공 메시지
    #     return super().form_valid(form)  # 폼 검사 결과를 반환