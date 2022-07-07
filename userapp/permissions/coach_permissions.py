from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import BasePermission

from userapp.models import Coach, User


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code = status_code
        super().__init__(detail=detail, code=code)


class IsAuthenticatedrIsAdmin(BasePermission):
    AVAILABLE_METHODS = ('GET', 'POST', 'DELETE')
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            response = {
                "detail": "서비스를 이용하기 위해 로그인 해주세요.",
            }
            raise GenericAPIException(status_code=status.HTTP_400_BAD_REQUEST, detail=response)

        if request.user.is_authenticated and request.method in self.AVAILABLE_METHODS:
            return True

        if request.user.is_admin and request.user:
            return True

