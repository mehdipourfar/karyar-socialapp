import shortuuid

from django.conf import settings
from django.db import models
from django.utils import timezone

from user.models import User


def generate_post_uid():
    return shortuuid.random(length=12)

# TODO: add edit post option
class Post(models.Model):
    uid = models.CharField(
        max_length=12,
        primary_key=True,
        default=generate_post_uid,
    )

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="posts")
    text = models.TextField(default="")
    image = models.ImageField(upload_to="images", default="", blank=True)
    timestamp = models.DateTimeField(
        default=timezone.now,
        db_index=True,
    )


class Comment(models.Model):
    uid = models.CharField(
        max_length=12,
        primary_key=True,
        default=generate_post_uid,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    text = models.TextField(default="")

    reply_to = models.ForeignKey(
        'post.Comment',
        on_delete=models.SET_NULL,
        null=True,
        related_name='replies',
    )

    timestamp = models.DateTimeField(
        default=timezone.now,
    )

    class Meta:
        index_together = ['post', 'timestamp']


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
