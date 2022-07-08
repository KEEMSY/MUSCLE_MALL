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

        if not request.user.is_authenticated or not request.user.approved_user:
            response = {
                "detail": "서비스는 유저만 이용 가능합니다.",
            }
            raise GenericAPIException(status_code=status.HTTP_400_BAD_REQUEST, detail=response)

        if request.user.is_authenticated or request.user.is_admin:
            return True

        return False
