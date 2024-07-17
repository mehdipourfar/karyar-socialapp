from rest_framework import viewsets

from .models import Post
from .serializer import PostViewSerializer

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes



@api_view(["GET"])
def list_posts(request: Request) -> Response:
    posts = Post.objects.order_by('-created_at').all()

    serializer = PostViewSerializer(posts, many=True)

    return Response(serializer.data)
