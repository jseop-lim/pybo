from itertools import chain

from django.db.models import F, Count
from django.shortcuts import render
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


class ProfileVoteListView(ProfileObjectListView):
    """
    작성한 댓글 목록
    """
    template_name = 'common/profile/profile_vote.html'
    profile_type = 'vote'

    def get_queryset(self):
        user = self.request.user
        question_list = user.voter_question.annotate(num_voter=Count('voter'))#.values('subject', 'create_date', 'category', 'num_voter')  # todo subject로 해도 왜 됨? 공식문서 읽기
        answer_list = user.voter_answer.annotate(category=F('question__category__description'), num_voter=Count('voter'))#.values('content', 'create_date', 'category', 'num_voter')  # todo 카테고리 어케 접근함?

        _queryset = sorted(
            chain(question_list, answer_list),
            key=lambda obj: obj.create_date,
            reverse=True,
        )
        return _queryset

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context.update({
            'profile_type': self.profile_type,
            # 'so': self.so
        })
        return context
