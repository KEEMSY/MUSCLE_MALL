from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from userapp.models import User, Coach
from userapp.serializers import UserSerializer, CoachSerializer
from userapp.services.user_service import get_user


class UserApiView(APIView):
    # 사용자 정보 조회 Done
    def get(self, request, user_id=None):
        user = get_user(user_id)
        if user:
            return Response(user, status=status.HTTP_200_OK)
        return Response({"msg": "유저가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
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

    # 사용자 삭제
    def delete(self, request):
        request_user = request.user
        user = get_object_or_404(User, id=request_user.id)
        user.delete()
        return Response({"msg": "회원탈퇴 완료"}, status=status.HTTP_200_OK)


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