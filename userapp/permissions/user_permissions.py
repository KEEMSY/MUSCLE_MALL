from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import BasePermission


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code = status_code
        super().__init__(detail=detail, code=code)


class IsAuthenticatedAndIsAprovedUser(BasePermission):
    ABAILIBLE_METHODS = ('GET', 'POST', 'DELETE')
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user

        if user.is_authenticated or request.method in self.ABAILIBLE_METHODS:
            return True

        if not user.is_authenticated:
            response = {
                "detail": "서비스를 이용하기 위해 로그인 해주세요.",
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if not user.approved_user:
            response = {
                "detail": "유저 승인 심사 중 입니다.",
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if user.is_authenticated or user.is_admin:
            return True



        return False
