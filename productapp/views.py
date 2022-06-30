from django.shortcuts import render

# Create your views here.
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from productapp.permissions import IsAdminOrReadOnly
from productapp.services.challenge_service import get_challenge, save_challenge, edit_challenge
from productapp.services.product_category_service import get_product_category, save_product_category, \
    edit_product_category, delete_product_category
from productapp.services.product_detail_category_service import get_product_detail_category, \
    save_product_detail_category, edit_product_detail_category, delete_product_delete_category
from productapp.services.product_service import get_product, save_product, edit_product, delete_product
from productapp.services.routine_service import get_routine, save_routine, edit_routine, delete_routine


class ProductCategoryApiView(APIView):
    def get(self, request, category_id=None):
        category = get_product_category(category_id)
        if category:
            return Response(category, status=status.HTTP_200_OK)
        return Response({'msg': "카테고리가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        product_category = save_product_category(**request.data)
        return Response(product_category, status=status.HTTP_201_CREATED)

    def put(self, request, category_id):
        product_category = edit_product_category(category_id, **request.data)
        if product_category:
            return Response(product_category, status=status.HTTP_201_CREATED)
        return Response({'msg': "카테고리가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, category_id):
        if delete_product_category(category_id):
            return Response({"msg": "삭제되었습니다."}, status=status.HTTP_200_OK)

        return Response({"msg": "카테고리가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)


class ProductDetailCategoryApiView(APIView):
    def get(self, request, detail_category=None, detail_category_id=None):
        category = get_product_detail_category(detail_category, detail_category_id)
        if category:
            return Response(category, status=status.HTTP_200_OK)

        return Response({'msg': "카테고리가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        detail_category = save_product_detail_category(**request.data)
        return Response(detail_category, status=status.HTTP_201_CREATED)

    def put(self, request, detail_category, detail_category_id):
        product_detail_category = edit_product_detail_category(detail_category, detail_category_id, **request.data)
        if product_detail_category:
            return Response(product_detail_category, status=status.HTTP_201_CREATED)
        return Response({'msg': "카테고리가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, detail_category, detail_category_id):
        category = delete_product_delete_category(detail_category, detail_category_id)
        if category:
            return Response({"msg": "삭제되었습니다."}, status=status.HTTP_200_OK)

        return Response({'msg': "카테고리가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)


class ProductApiView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, product_id=None):
        product = get_product(product_id)
        if product:
            return Response(product, status=status.HTTP_200_OK)
        return Response({'msg': "해당 하는 운동 / 음식이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        product = save_product(**request.data)
        return Response(product, status=status.HTTP_201_CREATED)

    def put(self, request, product_id):
        product = edit_product(product_id, **request.data)
        if product:
            return Response(product, status=status.HTTP_201_CREATED)
        return Response({'msg': "해당하는 운동 / 음식이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, product_id=None):
        user = request.user
        product = delete_product(user, product_id)
        if product:
            return Response({"msg": "삭제되었습니다."}, status=status.HTTP_200_OK)

        return Response({"msg": "올바른 접근이 아닙니다."}, status=status.HTTP_404_NOT_FOUND)


class RoutineApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # 현재 작성 중인 루틴 정보 조회
    def get(self, request, routine_id=None):
        user = request.user
        routine = get_routine(user, routine_id)
        if routine:
            return Response(routine, status=status.HTTP_200_OK)
        return Response({'msg': "루틴을 등록 해주세요"}, status=status.HTTP_404_NOT_FOUND)

    # 루틴 등록
    def post(self, request):
        user = request.user.id
        request.data["user"] = user
        routine = save_routine(**request.data)
        return Response(routine, status=status.HTTP_201_CREATED)

    # 루틴 수정
    def put(self, request, routine_id=None):
        user = request.user
        routine = edit_routine(user, routine_id, **request.data)
        if routine:
            return Response(routine, status=status.HTTP_200_OK)
        return Response({'msg': "루틴이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    # 루틴 삭제
    def delete(self, request, routine_id=None):
        user = request.user
        routine = delete_routine(user, routine_id)
        if routine:
            return Response({"msg": "삭제되었습니다."}, status=status.HTTP_200_OK)

        return Response({"msg": "올바른 접근이 아닙니다."}, status=status.HTTP_404_NOT_FOUND)


class ChallengeApiView(APIView):
    def get(self, request, challenge_id=None):
        user = request.user
        challenge = get_challenge(user, challenge_id)
        if challenge:
            return Response(challenge, status=status.HTTP_200_OK)

        return Response({'msg': "챌린지를 확인 해주세요"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        challenge = save_challenge(request.user.id)
        if challenge:
            return Response({"msg": "챌린지가 생성되었습니다."}, status=status.HTTP_201_CREATED)

        return Response({"msg": "올바른 접근이 아닙니다."}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, challenge_id):
        challenge = edit_challenge(request.user, challenge_id)
        if challenge:
            return Response(challenge, status=status.HTTP_200_OK)

        return Response({"msg": "챌린지가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        return Response({"msg": "delete method"})