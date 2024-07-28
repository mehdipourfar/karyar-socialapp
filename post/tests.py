from datetime import timedelta
from django.utils import timezone

from rest_framework.test import APITestCase

from .factories import PostFactory
from user.factories import UserFactory
from .models import Post

import time


class PostApiTests(APITestCase):

    def test_unauthorized_user_cannot_view_list(self):
        resp = self.client.get(
            "/api/posts/?limit=2",
        )

        self.assertEqual(401, resp.status_code)


    def test_list(self):
        ts = timezone.now()

        for i in range(10):
            PostFactory(timestamp=ts)
            ts += timedelta(milliseconds=1)

        user = UserFactory()

        self.client.force_authenticate(user)

        resp = self.client.get(
            "/api/posts/?limit=2",
        )

        self.assertEqual(200, resp.status_code)
        posts = resp.json()

        first_request_uids = [item['uid'] for item in posts]

        last_post_timestamp = posts[-1]['timestamp']

        resp = self.client.get(
            f"/api/posts/?limit=2&{last_post_timestamp=}"
        )

        posts = resp.json()

        new_uids = [item['uid'] for item in posts]


        for uid in first_request_uids:
            self.assertNotIn(uid, new_uids)

    def test_list_method_only_runs_single_sql_query(self):
        for i in range(10):
            PostFactory()

        user = UserFactory()
        self.client.force_authenticate(user)

        with self.assertNumQueries(1):
            response = self.client.get(f"/api/posts/")
            self.assertEqual(200, response.status_code)
