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

    coach_serializer = CoachSerializer(data=data)
    coach_serializer.is_valid(raise_exception=True)
    coach_serializer.save()

    return coach_serializer.data


def edit_coach(**data):
    try:
        coach = Coach.objects.get(user=data["user"])
        if not coach.approved_coach:
            raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND)

        coach_serializer = CoachSerializer(coach, data=data, partial=True)
        coach_serializer.is_valid(raise_exception=True)
        coach_serializer.save()
        return coach_serializer.data

    except ObjectDoesNotExist:
        response = {
            "detail": "코치를 먼저 생성해 주세요.",
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)

    except GenericAPIException:
        response = {
            "detail": "코치 승인 심사 중 입니다.",
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)


def delete_coach(user):
    try:
        coach = Coach.objects.get(user=user)
        coach.delete()
        return True

    except ObjectDoesNotExist:
        response = {
            "detail": "해당 코치정보가 존재하지 않습니다.",
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)