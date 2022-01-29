from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from pybo.models import *

#
# class AnswerViewTests(TestCase):
#     def test_rewrite_answer_page_passed(self):
#         """
#         답변 입력 형식이 올바르지 않을 때, GET 요청 시 올바르게 페이지가 url로 전달되는지 검사
#         """
#         pass


# def get_page_sql(self, so='recommend'):
#     # https://stackoverflow.com/questions/1042596/get-the-index-of-an-element-in-a-queryset
#
#     queryset = Answer.order_by_so(self.question.answer_set.all(), so)
#
#     if so == 'recommend':
#         order_by = '"num_voter" DESC, "create_date" DESC'
#     else:
#         order_by = '"create_date" DESC'
#
#     numbered_qs = queryset.extra(select={
#         'row_num': f'ROW_NUMBER() OVER (ORDER BY {order_by})'
#     })
#
#     from django.db import connection
#     with connection.cursor() as cursor:
#         cursor.execute(
#             f"WITH OrderedQueryset AS ({numbered_qs.query}) SELECT row_num FROM OrderedQueryset WHERE id = {self.id}"
#         )
#         index = cursor.fetchall()[0][0]
#
#     return (index - 1) // 5 + 1


class AnswerModelTests(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username='testuser1', password='1234')
        # self.client.login(username='testuser', password='1234')
        self.voter = User.objects.create_user(username='testuser2', password='1234')

        Category.objects.create(name='cat1')

        Question.objects.create(subject='test question', content='question content',
                                author_id=1, create_date=timezone.now(), category_id=1)
        NUM_ANSWER = 12
        for i in range(NUM_ANSWER):
            answer = Answer.objects.create(content=f'test answer[{i+1}]', question_id=1, author_id=1, create_date=timezone.now())
            if (i+1) % 2 == 1:
                answer.voter.add(self.voter)

    # def test_get_page(self):
    #     for answer in Answer.objects.all():
    #         with self.subTest(answer=answer):
    #             self.assertEqual(answer.get_page('recommend'), get_page_sql(answer, 'recommend'), msg=f'{answer.content}')


