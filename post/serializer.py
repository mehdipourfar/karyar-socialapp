from rest_framework import serializers

from .models import Post

from user.serializers import UserSerializer
from utils.funcs import datetime_to_unixtime


class PostViewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    timestamp = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['uid', 'text', 'image', 'user', 'timestamp']

    def get_timestamp(self, obj: Post) -> int:
        return datetime_to_unixtime(obj.timestamp)
