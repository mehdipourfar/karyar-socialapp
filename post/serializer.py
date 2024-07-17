from rest_framework import serializers

from .models import Post

from user.serializers import UserSerializer


class PostViewSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = ['id', 'text', 'image', 'user']


# def serialize_v2(post):
#     return {
#         "id": post.id,
#         "text": post.text,
#         "image": post.image.url
#     }
