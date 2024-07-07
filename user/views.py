import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .serializers import  UserSerializer



@api_view(['POST'])
def register(request: Request) -> Response:
    serializer = UserSerializer(
        data=request.data,
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=200)
