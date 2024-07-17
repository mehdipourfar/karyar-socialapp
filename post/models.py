from django.db import models

from user.models import User


# TODO: add edit post option
class Post(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="posts")
    text = models.TextField(default="")
    image = models.ImageField(upload_to="images", default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
