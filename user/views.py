import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User



@api_view(['POST'])
def register(request: Request) -> Response:

    User.objects.create_user(
        username=request.data.get("username"),
        password=request.data.get("password")
    )

    return Response(status=200)
