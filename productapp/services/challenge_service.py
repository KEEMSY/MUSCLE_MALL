from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from productapp.models import Challenge, Routine
from productapp.serializers import ChallengeSerializer
from userapp.models import User
from userapp.services.user_service import edit_user


def get_challenge(user, challenge_id=None):
    if challenge_id:
        try:
            challenge = Challenge.objects.get(id=challenge_id, user=user)
            challenge_serializer = ChallengeSerializer(challenge).data
            return challenge_serializer

        except ObjectDoesNotExist:
            return False

    try:
        challenges = Challenge.objects.filter(user=user)
        challenges_serializer = ChallengeSerializer(challenges, many=True).data
        return challenges_serializer

    except ObjectDoesNotExist:
        return False


@transaction.atomic
def save_challenge(user_id):
    routines = Routine.objects.filter(user=user_id)
    user = User.objects.get(id=user_id)

    if len(routines):
        data = {
            "user": user_id,
            "bind_number": user.bind_number
        }

        for routine in routines:
            data["product"] = routine.product.id
            challenge_serializer = ChallengeSerializer(data=data)

            challenge_serializer.is_valid(raise_exception=True)
            challenge_serializer.save()
            routine.delete()

        if edit_user(user_id, **data):
            return True

    else:
        return False


def edit_challenge(user, challenge_id):
    try:
        challenge = Challenge.objects.get(user=user, id=challenge_id)
        data = {}
        if challenge.status == "시작 전":
            data["status"] = "진행 중"
        else:
            data["status"] = "완료"

        challenge_serializer = ChallengeSerializer(challenge, data=data, partial=True)
        challenge_serializer.is_valid(raise_exception=True)
        challenge_serializer.save()
        return challenge_serializer.data

    except ObjectDoesNotExist:
        return False


def delete_challenge(user, challenge_id=None):
    if challenge_id:
        try:
            challenge = Challenge.objects.get(user=user, id=challenge_id)
            challenge.delete()
            return True
        except ObjectDoesNotExist:
            return False
    else:
        try:
            challenge = Challenge.objects.filter(user=user)
            challenge.delete()
            return True
        except ObjectDoesNotExist:
            return False
