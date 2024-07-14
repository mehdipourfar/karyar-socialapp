import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils import timezone

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from django.contrib.auth import authenticate

from .models import User
from .serializers import  UserSerializer, LoginSerializer



@api_view(['POST'])
@permission_classes([AllowAny])
def register(request: Request) -> Response:
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=200)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request: Request) -> Response:
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data = serializer.validated_data

    try:
        user = User.objects.get(username=data['username'])
    except User.DoesNotExist:
        return Response({"error": "username or password is incorrect"}, status=400)


    if not user.check_password(data['password']):
        return Response({"error": "username or password is incorrect"}, status=400)


    token, _ = Token.objects.get_or_create(
        user=user,
        defaults={'key': Token.generate_key()},
    )

    user.last_login = timezone.now()
    user.save()

    return Response({"token": token.key})
