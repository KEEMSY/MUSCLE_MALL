from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from userapp.models import User, Coach
from userapp.permissions.coach_permissions import  IsAuthenticatedrIsAdmin
from userapp.permissions.user_permissions import IsAuthenticatedAndIsAprovedUser
from userapp.serializers import UserSerializer, CoachSerializer
from userapp.services.coach_service import get_coach, save_coach, edit_coach, delete_coach
from userapp.services.user_service import get_user, save_user, delete_user, edit_user


class UserApiView(APIView):
    permission_classes = [IsAuthenticatedAndIsAprovedUser]

    # 사용자 정보 조회 Done
    def get(self, request, user_id=None):
        user = get_user(user_id)
        if user:
            return Response(user, status=status.HTTP_200_OK)
        return Response({"msg": "유저가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    # 회원가입 Done
    def post(self, request):
        user = save_user(**request.data)
        return Response(user, status=status.HTTP_201_CREATED)

    # 사용자 정보 수정 Done
    def put(self, request):
        user = edit_user(request.user.id, **request.data)
        if user:
            return Response(user, status=status.HTTP_200_OK)

        return Response({"msg": "올바지르 못한 접근 입니다."}, status=status.HTTP_400_BAD_REQUEST)

    # 사용자 삭제
    def delete(self, request):
        if delete_user(request.user.id):
            return Response({"msg": "회원탈퇴 완료"}, status=status.HTTP_200_OK)
        return Response({"msg": "유저가 존재하지 않습니다."})


class UserView(APIView):
    # 로그인
    def post(self, request):
        user = authenticate(request, **request.data)
        if not user:
            return Response({"error": "회원정보를 확인해주세요"}, status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        return Response({"msg": "로그인 성공"}, status=status.HTTP_200_OK)

    # 로그아웃
    def delete(self, request):
        logout(request)
        return Response({"msg": "로그아웃 성공"}, status=status.HTTP_200_OK)


class CoachApiView(APIView):
    permission_classes = [IsAuthenticatedrIsAdmin]

    def get(self, request, coach_id=None):
        coach = get_coach(coach_id)
        if coach:
            return Response(coach, status=status.HTTP_200_OK)

        return Response({"msg": "존재하지 않는 코치입니다."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        request.data['user'] = request.user.id
        coach = save_coach(**request.data)
        if coach:
            return Response(coach, status=status.HTTP_201_CREATED)

    def put(self, request):
        request.data['user'] = request.user.id
        coach = edit_coach(**request.data)
        return Response(coach, status=status.HTTP_200_OK)

    def delete(self, request):
        if delete_coach(request.user.id):
            return Response({"msg": "삭제되었습니다."}, status=status.HTTP_200_OK)

