from django.test import TestCase

from userapp.models import User
from userapp.services.user_service import get_user, save_user


class TestUserService(TestCase):
    def test_get_user_when_user_id_is_exist(self):
        # given
        user = User.objects.create(
            username="test_username",
            email="test@email.com",
            password="1234",
            fullname="test_fullname",
            gender="male"
        )

        # when
        user_id = user.id
        expected_user = get_user(user_id)

        # expect
        self.assertEqual(expected_user["username"], user.username)

    def test_save_user(self):
        # when
        data = {
            "username": "test_username",
            "email": "test@email.com",
            "password": "1234",
            "fullname": "test_fullname",
            "gender": "male"
        }
        user = save_user(**data)

        # expect
        self.assertIsNotNone(User)
        self.assertEqual(data["username"], user["username"])
