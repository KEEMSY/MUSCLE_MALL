from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from productapp.models import Challenge, Routine
from productapp.serializers import ChallengeSerializer


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
    # try가 아니고 길이로 확인해야할 듯
    try:
        routines = Routine.objects.filter(user=user_id)
        data = {
            "user": user_id,
        }
        for routine in routines:
            data["routine"] = routine.id
            challenge_serializer = ChallengeSerializer(data=data)

            challenge_serializer.is_valid(raise_exception=True)
            challenge_serializer.save()
            routine.delete()

        return True

    except ObjectDoesNotExist:
        return False


def edit_challenge(user, challenge_id):
    try:
        challenge = Challenge.objects.get(user=user, id=challenge_id)
        data = {}
        if challenge.status == "시작 전":
            data["status"] = "진행 중"
        else:
            data["status"] = "완료"

        challenge_serializer = ChallengeSerializer(challenge, data=data,partial=True)
        challenge_serializer.is_valid(raise_exception=True)
        challenge_serializer.save()
        return challenge_serializer.data

    except ObjectDoesNotExist:
        return False