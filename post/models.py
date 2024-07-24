import shortuuid

from django.db import models

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
        auto_now_add=True,
        db_index=True,
    )
