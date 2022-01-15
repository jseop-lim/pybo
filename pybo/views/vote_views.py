from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, resolve_url

from ..models import Question, Answer


@login_required(login_url='login')
def vote_question(request, question_id):
    """
    pybo 질문추천등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글을 추천할 수 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect(question)


@login_required(login_url='login')
def vote_answer(request, answer_id):
    """
    pybo 답변추천등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글을 추천할 수 없습니다.')
    else:
        answer.voter.add(request.user)
    # todo 추천 시 답변 목록의 페이지 유지하기
    return redirect(f"{resolve_url(answer.question)}#answer_start")