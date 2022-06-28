import random

from django.core.exceptions import ObjectDoesNotExist

from productapp.models import Routine
from productapp.serializers import RoutineSerializer
from userapp.models import User


def get_routine(user, routine_id=None):
    if routine_id:
        try:
            routine = Routine.objects.get(id=routine_id, user=user)
            routine_serializer = RoutineSerializer(routine).data
            return routine_serializer

        except ObjectDoesNotExist:
            return False

    try:
        routines = Routine.objects.filter(user=user)
        routines_serializer = RoutineSerializer(routines, many=True).data
        return routines_serializer

    except ObjectDoesNotExist:
        return False
