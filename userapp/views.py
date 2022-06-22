from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from userapp.serializers import UserSerializer


class UserApiView(APIView):
    def get(self, request):
        return Response()

    # 회원가입
    def post(self, request):
        user_serializer = UserSerializer(request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        return Response()

    def delete(self, request):
        return Response()
