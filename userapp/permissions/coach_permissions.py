from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import BasePermission

from userapp.models import Coach


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code = status_code
        super().__init__(detail=detail, code=code)

# 수정이 필요함
class IsAuthenticatedAndIsAprovedCoach(BasePermission):
    ABAILIBLE_METHODS = ('GET', 'POST', 'DELETE')
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user_id = request.user.id
        coach = Coach.objects.get(user_id=user_id)

        if not coach.user.is_authenticated:
            response = {
                "detail": "서비스를 이용하기 위해 로그인 해주세요.",
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if not coach.user.approved_user or  not coach.approved_coach:
            response = {
                "detail": "유저 승인 심사 중 입니다.",
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if coach.user.is_authenticated or coach.user.is_admin:
            return True

        if coach.user.is_authenticated and request.method in self.ABAILIBLE_METHODS:
            return True

        return False
