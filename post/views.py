from rest_framework import viewsets

from .models import Post
from .serializer import PostViewSerializer

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


@api_view(["GET"])
def list_posts(request: Request) -> Response:
    limit = int_or_default(request.query_params.get("limit"), 10)
    last_post_id = int_or_default(request.query_params.get("last_post_id"), 0)

    if limit > 10:
        limit = 10

    posts = Post.objects.all()

    if last_post_id:
        posts = posts.filter(id__lt=last_post_id)

    posts = posts.order_by('-id')[:limit]

    serializer = PostViewSerializer(posts, many=True)

    return Response(serializer.data)


def int_or_default(value: str, default: int) -> int:
    try:
        value = int(value)
        if value < 0:
            return default
        return value
    except (ValueError, TypeError):
        return default
