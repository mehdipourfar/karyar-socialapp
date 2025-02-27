"""
URL configuration for socialapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter

from user import views as user_views
import post.views as post_views


# router = DefaultRouter()

# router.register(r"posts", PostViewSet, basename="posts")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/register/", user_views.register),
    path("user/login/", user_views.login),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/', include(router.urls)),
    path('api/posts/', post_views.list_posts),
]

if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
