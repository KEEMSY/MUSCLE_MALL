from django.core.exceptions import ObjectDoesNotExist

from userapp.models import Coach
from userapp.serializers import CoachSerializer


def get_coach(coach_id=None):
    if coach_id:
        try:
            coach = Coach.objects.get(id=coach_id)
            if coach.approved_user:
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
