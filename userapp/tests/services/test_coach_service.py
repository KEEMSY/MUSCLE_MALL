from django.test import TestCase

from userapp.models import User, Coach
from userapp.services.coach_service import get_coach, save_coach, edit_coach, delete_coach


class TestCoachService(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCoachService, self).__init__(*args, **kwargs)
        self.coach_data = {
            "nickname": "WeightKing",
            "phone_number": "010-1234-1234",
            "kind": "fitness"
        }

        self.coach_update_data = {
            "nickname": "WeightQueen"
        }

    def make_user(self):
        user = User.objects.create(
            username="test_username1",
            email="test@email.com",
            password="1234",
            fullname="test_fullname",
            gender="male",
            approved_user="True"
        )
        return user


    # Coach 조회
    def test_get_coach_when_coach_does_not_exist(self):
        # given
        user = self.make_user()

        # when
        coach = get_coach()

        # expect
        self.assertEqual(0, len(coach))

    def test_save_coach_only_approved_user(self):
        # given
        user = self.make_user()
        self.coach_data["user"] = user.id

        # when
        coach = save_coach(**self.coach_data)
        coach.pop("approved_coach")

        # expect
        self.assertEqual(self.coach_data, coach)

    def test_can_not_save_coach_not_approved_user(self):
        # given
        user = self.make_user()
        self.coach_data["user"] = user.id

        # when
        user.approved_user = False
        user.save()
        not_coach = save_coach(**self.coach_data)

        # expect
        self.assertEqual(False, not_coach)

    def test_edit_coach_only_approved_coach(self):
        # given
        user = self.make_user()

        coach_data = self.coach_data
        coach_data["user"] = user.id
        save_coach(**coach_data)

        coach = Coach.objects.get(user=user)
        coach.approved_coach = True
        coach.save()

        # when
        coach_update_data = self.coach_update_data
        coach_update_data["user"] = user.id
        update_coach = edit_coach(**coach_update_data)

        # expect
        self.assertEqual(self.coach_update_data["nickname"], update_coach["nickname"])

    def test_delete_coach(self):
        # give
        user = self.make_user()
        coach_data = self.coach_data
        coach_data["user"] = user.id
        save_coach(**coach_data)

        # when
        delete_coach(user)

        # expect
        with self.assertRaises(Coach.DoesNotExist):
            Coach.objects.get(user=user)