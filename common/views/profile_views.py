from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from pybo.models import Question, Answer, Comment


def profile_base(request):
    """
    프로필 기본정보
    """
    context = {'user': request.user, 'profile_type': 'base'}
    return render(request, 'common/profile/profile_base.html', context)


class ProfileObjectListView(ListView):
    """
    프로필 목록 추상 클래스 뷰
    """
    paginate_by = 10

    class Meta:
        abstract = True

    def get_queryset(self):
        self.so = self.request.GET.get('so', 'recent')  # 정렬기준
        object_list = self.model.objects.filter(author=self.request.user)
        # 정렬
        object_list = Answer.order_by_so(object_list, self.so)
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'profile_type': self.profile_type,
            'so': self.so
        })
        return context


class ProfileQuestionListView(ProfileObjectListView):
    """
    작성한 질문 목록
    """
    model = Question
    template_name = 'common/profile/profile_question.html'
    profile_type = 'question'


class ProfileAnswerListView(ProfileObjectListView):
    """
    작성한 답변 목록
    """
    model = Answer
    template_name = 'common/profile/profile_answer.html'
    profile_type = 'answer'


class ProfileCommentListView(ProfileObjectListView):
    """
    작성한 댓글 목록
    """
    model = Comment
    template_name = 'common/profile/profile_comment.html'
    profile_type = 'comment'

