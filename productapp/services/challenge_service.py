from django.core.exceptions import ObjectDoesNotExist

from productapp.models import Challenge
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