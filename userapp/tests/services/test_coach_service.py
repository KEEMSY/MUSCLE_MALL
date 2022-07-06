from django.test import TestCase

from userapp.models import User
from userapp.services.coach_service import get_coach


class TestCoachService(TestCase):
    coach_data = {
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

    # Coach 생성
    def test_save_coach(self):
        # given
        user = self.make_user()
        # sava_coach =
        # when
        # expect