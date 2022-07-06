from django.test import TestCase

from userapp.models import User
from userapp.services.coach_service import get_coach, save_coach


class TestCoachService(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCoachService, self).__init__(*args, **kwargs)
        self.coach_data = {
            "nickname": "WeightKing",
            "phone_number": "010-1234-1234",
            "kind": "fitness"
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
