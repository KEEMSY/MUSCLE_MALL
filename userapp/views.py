from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from userapp.models import User, Coach
from userapp.serializers import UserSerializer, CoachSerializer
from userapp.services.user_service import get_user, save_user, delete_user, edit_user


class UserApiView(APIView):
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, user_id=None):
        if user_id:
            try:
                coach = Coach.objects.get(user_id=user_id)
                coach_serializer = CoachSerializer(coach).data
                return Response(coach_serializer, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({"msg": "존재하지 않는 코치입니다."}, status=status.HTTP_404_NOT_FOUND)

        coachs = Coach.objects.all()
        if len(coachs):
            coach_serializer = CoachSerializer(coachs, many=True).data
            return Response(coach_serializer, status=status.HTTP_200_OK)
        return Response({"msg": "현재 코치가 존재하지 않습니다."})

    def post(self, request):
        request.data['user'] = request.user.id
        coach_serializer = CoachSerializer(data=request.data)
        coach_serializer.is_valid(raise_exception=True)
        coach_serializer.save()
        return Response(coach_serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        try:
            coach = Coach.objects.get(user=request.user)
            coach_serializer = CoachSerializer(coach, data=request.data, partial=True)
            if coach_serializer.is_valid():
                coach_serializer.save()
                return Response({"msg": "변경되었습니다."}, status=status.HTTP_200_OK)

            return Response(coach_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response({"msg": "잘못된 접근입니다."}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            coach = Coach.objects.get(user=request.user)
            coach.delete()
            return Response({"msg": "삭제되었습니다."}, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({"msg": "코치가 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)