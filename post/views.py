from rest_framework import viewsets

from .models import Post
from .serializer import PostViewSerializer

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from utils.funcs import unixtime_to_datetime, int_or_default


@api_view(["GET"])
def list_posts(request: Request) -> Response:
    limit = int_or_default(request.query_params.get("limit"), 10)
    last_post_timestamp = int_or_default(
        request.query_params.get("last_post_timestamp"), 0,
    )

    if limit > 10:
        limit = 10

    posts = Post.objects.all()

    if last_post_timestamp:
        posts = posts.filter(
            timestamp__lt=unixtime_to_datetime(last_post_timestamp)
        )

    posts = posts.select_related('user').order_by('-timestamp')[:limit]

    serializer = PostViewSerializer(posts, many=True)

    return Response(serializer.data)
