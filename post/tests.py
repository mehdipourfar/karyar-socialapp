from rest_framework.test import APITestCase

from .factories import PostFactory


class PostApiTests(APITestCase):
    def test_list(self):
        PostFactory()
