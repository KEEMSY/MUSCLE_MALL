from django.core.exceptions import ObjectDoesNotExist

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


def save_challenge(**kwargs):
    routine = kwargs["routine"]
    try:
        user_routine = Routine.objects.get(id=routine).user.id
        if user_routine == kwargs["user"]:
            challenge_serializer = ChallengeSerializer(data=kwargs)
            challenge_serializer.is_valid(raise_exception=True)
            challenge_serializer.save()
            return challenge_serializer.data

        return False

    except ObjectDoesNotExist:
        return False
