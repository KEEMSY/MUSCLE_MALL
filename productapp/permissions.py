from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status

from userapp.models import Coach


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code = status_code
        super().__init__(detail=detail, code=code)


class IsAdminOrIsAuthenticatedAndIsCoachOrReadOnly(BasePermission):
    SAFE_METHODS = ('GET',)
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response = {
                "detail": "서비스를 이용하기 위해 로그인 해주세요.",
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if user.is_authenticated and request.method in self.SAFE_METHODS or user.is_admin:
            return True

        if user.is_authenticated:
            try:
                coach = Coach.objects.get(user=user)
                return True
            except ObjectDoesNotExist:
                response = {
                    "detail": "서비스 이용을 위해 코치 등록을 해주세요.",
                }
                raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)
