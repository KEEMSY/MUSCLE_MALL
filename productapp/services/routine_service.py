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


def save_routine(**kwargs):
    routine_serializer = RoutineSerializer(data=kwargs)
    routine_serializer.is_valid(raise_exception=True)
    routine_serializer.save()
    return routine_serializer.data


def edit_routine(user, routine_id, **kwargs):
    try:
        routine = Routine.objects.get(user=user, id=routine_id)
        routine_serializer = RoutineSerializer(routine, data=kwargs, partial=True)
        routine_serializer.is_valid(raise_exception=True)
        routine_serializer.save()
        return routine_serializer.data

    except ObjectDoesNotExist:
        return False