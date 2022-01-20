from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from pybo.models import Question, User
from django.db.models import Count


def profile_base(request):
    """
    프로필 기본정보
    """
    context = {'user': request.user, 'profile_type': 'base'}
    return render(request, 'common/profile/profile_base.html', context)


class ProfileQuestionListView(ListView):
    """
    프로필 질문 목록
    """
    paginate_by = 10
    context_object_name = 'question_list'
    template_name = 'common/profile/profile_question.html'

    def get_queryset(self):
        self.so = self.request.GET.get('so', 'recent')  # 정렬기준
        _question_list = Question.objects.filter(author=self.request.user)

        # 정렬
        if self.so == 'recent':
            # aggretation, annotation에는 relationship에 대한 역방향 참조도 가능 (ex. Count('voter'))
            _question_list = _question_list.order_by('-create_date')
        elif self.so == 'recommend':
            _question_list = _question_list.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')

        return _question_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_type'] = 'question'
        context['so'] = self.so
        return context
