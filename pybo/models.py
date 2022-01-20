from django.db import models
from django.db.models import Count
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    has_answer = models.BooleanField(default=True)  # 답변가능 여부

    # def __str__(self):
    #     return self.name
    # return self.description

    def get_absolute_url(self):
        return reverse('pybo:index', args=[self.name])


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_question')

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('pybo:detail', args=[self.id])


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')  # 추천인 추가

    def __str__(self):
        return self.content

    def get_page(self):
        # todo MySQL 연동 후에 raw SQL로 대체
        # https://stackoverflow.com/questions/1042596/get-the-index-of-an-element-in-a-queryset
        index = 0
        for _answer in self.question.answer_set.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date'):
            index += 1
            if self == _answer:
                break

        return (index - 1)//5 + 1

    def get_absolute_url(self):
        return reverse('pybo:detail', args=[self.question.id]) + f'?page={self.get_page()}&so=recommend#answer_{self.id}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        if self.question:
            return reverse('pybo:detail', args=[self.question.id]) + '#comment_question_start'
        else:  # if self.answer:
            return reverse('pybo:detail', args=[self.answer.question.id]) + \
                   f'?page={self.answer.get_page()}&so=recommend#answer_{self.answer.id}'  # todo comment_id 가능?
