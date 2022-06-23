from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from userapp.models import User
from userapp.serializers import UserSerializer


class UserApiView(APIView):
    # 사용자 정보 조회
    def get(self, request, user_id=None):
        if user_id:
            user_serializer = UserSerializer(User.objects.get(id=user_id)).data
            return Response(user_serializer, status=status.HTTP_200_OK)
        users = UserSerializer(User.objects.all(), many=True).data
        return Response(users, status=status.HTTP_200_OK)

    # 회원가입 Done
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

    # 사용자 정보 수정 Done
    def put(self, request, user_id):
        user = request.user
        target_user_id = User.objects.get(id=user_id).id
        if user.is_anonymous:
            return Response({"error": "로그인 후 이용해주세요"}, status=status.HTTP_400_BAD_REQUEST)
        elif user.id != target_user_id:
            return Response({"error": "올바르지 못한 접근입니다."}, status=status.HTTP_400_BAD_REQUEST)

        user_serilaizer = UserSerializer(user, data=request.data, partial=True)
        if user_serilaizer.is_valid():
            user_serilaizer.save()
            return Response({"msg": "수정되었습니다."}, status=status.HTTP_200_OK)

        return Response(user_serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 사욪자 삭제
    def delete(self, request):
        return Response({"msg": "delete method!"})


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
