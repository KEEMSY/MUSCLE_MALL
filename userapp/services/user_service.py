from django.core.exceptions import ObjectDoesNotExist

from userapp.models import User
from userapp.serializers import UserSerializer


def get_user(user_id=None):
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            user_serializer = UserSerializer(user).data
            return user_serializer
        except ObjectDoesNotExist:
            return False
    try:
        users = UserSerializer(User.objects.all(), many=True).data
        return users

    except ObjectDoesNotExist:
        return False


def save_user(**data):
    user_serializer = UserSerializer(data=data)
    user_serializer.is_valid(raise_exception=True)
    user_serializer.save()
    return user_serializer.data


def edit_user(user_id, **data):
    try:
        user = User.objects.get(id=user_id)
        user_serilaizer = UserSerializer(user, data=data, partial=True)
        user_serilaizer.is_valid(raise_exception=True)
        user_serilaizer.save()
        return True
    except ObjectDoesNotExist:
        return False
