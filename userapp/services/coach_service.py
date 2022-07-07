from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

from userapp.models import Coach, User
from userapp.permissions.coach_permissions import GenericAPIException
from userapp.serializers import CoachSerializer


def get_coach(coach_id=None):
    if coach_id:
        try:
            coach = Coach.objects.get(id=coach_id)
            if coach.approved_coach:
                coach_serializer = CoachSerializer(coach).data
                return coach_serializer

            return False

        except ObjectDoesNotExist:
            return False
    try:
        approved_coach = []
        coachs = Coach.objects.all()
        for coach in coachs:
            if coach.approved_coach:
                approved_coach.append(coach)

        coachs = CoachSerializer(approved_coach, many=True).data

        return coachs

    except ObjectDoesNotExist:
        return False


def save_coach(**data):
    user = User.objects.get(id=data['user'])
    if not user.approved_user:
        response = {
            "detail": "유저 심사 중입니다.",
        }
        raise GenericAPIException(status_code=status.HTTP_400_BAD_REQUEST, detail=response)

    coach_serializer = CoachSerializer(data=data)
    coach_serializer.is_valid(raise_exception=True)
    coach_serializer.save()

    return coach_serializer.data