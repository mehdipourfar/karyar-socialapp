from django.test import TestCase
from django.utils import timezone

from rest_framework.test import APITestCase

from .models import User



class UserApiTests(APITestCase):
    def test_register(self):
        resp = self.client.post(
            "/user/register/",
            data={"username": "good_user", "password": "bad_password"},
        )

        self.assertEqual(resp.status_code, 200)

        user = User.objects.get(username="good_user")
        self.assertTrue(user.check_password("bad_password"))

    def test_register_does_not_work_with_get_method(self):
        resp = self.client.get(
            "/user/register/",
            data={"username": "good_user", "password": "bad_password"},
        )

        self.assertEqual(resp.status_code, 405)

    def test_user_cannot_register_with_already_registered_username(self):
        User.objects.create_user(username="good_user")

        resp = self.client.post(
            "/user/register/",
            data={"username": "good_user", "password": "bad_password"},
        )

        self.assertEqual(resp.status_code, 400)



    def test_login(self):
        User.objects.create_user(username="good_user", password="bad_password")

        resp = self.client.post(
            "/user/login/",
            data={"username": "good_user", "password": "bad_password"},
        )

        self.assertEqual(resp.status_code, 200)
        self.assertIn("token", resp.json())


    def test_last_login_is_set_after_each_login(self):
        user = User.objects.create_user(
            username="good_user",
            password="bad_password",
        )
        user.last_login = timezone.now()
        user.save()

        last_login = user.last_login

        resp = self.client.post(
            "/user/login/",
            data={"username": "good_user", "password": "bad_password"},
        )

        user.refresh_from_db()

        self.assertGreater(user.last_login, last_login)
