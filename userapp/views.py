from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from userapp.serializers import UserSerializer


class UserApiView(APIView):
    # 사용자 정보 조회
    def get(self, request):
        return Response({"msg": "get method!"})

    # 회원가입
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

    # 사용자 정보 수정
    def put(self, request):
        return Response({"msg": "put method!"})

    # 사욪자 삭제
    def delete(self, request):
        return Response({"msg": "delete method!"})

