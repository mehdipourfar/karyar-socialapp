import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt


from .models import User




@csrf_exempt
def register(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return HttpResponse(status=405)

    body = json.loads(request.body)

    username = body.get("username")
    password = body.get("password")

    print(username)
    print(password)

    return HttpResponse(status=200, content)
