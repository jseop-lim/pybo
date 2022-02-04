import os
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def get_file_path(instance, filename):
    user_id = instance.user_id
    uuid_name = uuid4().hex
    ext = os.path.splitext(filename)[-1]
    return f'common/profile/{user_id}/{uuid_name}{ext}'


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# todo 질문목록, 질문상세, 댓글에서 프로필 사진보이게

