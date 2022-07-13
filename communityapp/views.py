from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from communityapp.services.board_category_service import get_board_category, save_board_category, edit_board_category, \
    delete_board_category
from communityapp.services.board_service import get_board


class BoardCategoryApiView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, category_id=None):
        category = get_board_category(category_id)
        return Response(category, status=status.HTTP_200_OK)

    def post(self, request):
        category = save_board_category(**request.data)
        return Response(category, status=status.HTTP_201_CREATED)

    def put(self, request, category_id):
        category = edit_board_category(category_id, **request.data)
        return Response(category, status=status.HTTP_200_OK)

    def delete(self, request, category_id):
        category = delete_board_category(category_id)
        return Response({'msg': '삭제되었습니다.'})


class BoardApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, category_id=None, board_id=None):
        board = get_board(category_id=None, board_id=None)
        if not len(board):
            return Response({'msg': '게시글이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)

        return Response(board, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({"msg": "post method"})

    def put(self, request):
        return Response({"msg": "put method"})

    def delete(self, request):
        return Response({"msg": "delete method"})