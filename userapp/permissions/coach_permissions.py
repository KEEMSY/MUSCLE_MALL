from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import BasePermission

from userapp.models import Coach, User


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code = status_code
        super().__init__(detail=detail, code=code)


class IsAuthenticatedAndIsAprovedCoach(BasePermission):
    ABAILIBLE_METHODS = ('GET', 'POST', 'DELETE')
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = User.objects.get(id=request.user.id)

        if not user.is_authenticated:
            response = {
                "detail": "서비스를 이용하기 위해 로그인 해주세요.",
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        try:
            coach = Coach.objects.get(user_id=user.id)
            if not coach.approved_coach:
                response = {
                    "detail": "코치 승인 심사 중 입니다.",
                }
                raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

            if coach.approved_coach or coach.user.is_admin:
                return True

            return False

        except Exception:
            if request.method in self.ABAILIBLE_METHODS or user.is_admin:
                return True

            return False




