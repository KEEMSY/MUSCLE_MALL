from django.test import TestCase

from userapp.models import User
from userapp.services.user_service import get_user, save_user, delete_user


class TestUserService(TestCase):
    def test_get_user_when_user_id_is_exist_or_not(self):
        # given
        user1 = User.objects.create(
            username="test_username1",
            email="test@email.com",
            password="1234",
            fullname="test_fullname",
            gender="male",
            approved_user="True"
        )

        user2 = User.objects.create(
            username="test_usernam2",
            email="test@email.com",
            password="1234",
            fullname="test_fullname",
            gender="male",
            approved_user="True"
        )

        # when
        user_id = user1.id
        expected_user = get_user(user_id)
        expected_users = get_user()

        # expect
        self.assertEqual(expected_user["username"], user1.username)
        self.assertEqual(2, len(expected_users))

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

    def test_delete_user(self):
        # given
        data = {
            "username": "test_username",
            "email": "test@email.com",
            "password": "1234",
            "fullname": "test_fullname",
            "gender": "male"
        }
        target_username = save_user(**data)["username"]
        target_user = User.objects.get(username=target_username)

        # when
        expect = delete_user(target_user.id)

        # expect
        self.assertEqual(True, expect)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username=target_username)
