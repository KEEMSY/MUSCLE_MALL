from django.core.exceptions import ObjectDoesNotExist

from userapp.models import User
from userapp.serializers import UserSerializer


def edit_user(user_id, **data):
    try:
        user = User.objects.get(id=user_id)
        user_serilaizer = UserSerializer(user, data=data, partial=True)
        user_serilaizer.is_valid(raise_exception=True)
        user_serilaizer.save()
        return True
    except ObjectDoesNotExist:
        return False
