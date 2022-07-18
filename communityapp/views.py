from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from communityapp.services.board_category_service import get_board_category, save_board_category, edit_board_category, \
    delete_board_category
from communityapp.services.board_service import get_board, save_board, edit_board, delete_board
from communityapp.services.comment_service import get_comment, save_comment, edit_comment, delete_comment


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

    def get(self, request, category_kind=None, board_id=None):
        board = get_board(category_kind, board_id)
        if not len(board):
            return Response({'msg': '게시글이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)

        return Response(board, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['user'] = request.user.id
        board = save_board(**request.data)
        return Response(board, status=status.HTTP_201_CREATED)

    def put(self, request, board_id):
        request.data['user'] = request.user.id
        board = edit_board(board_id, **request.data)
        return Response(board, status=status.HTTP_200_OK)

    def delete(self, request, board_id):
        delete_board(request.user.id, board_id)
        return Response({"msg": "게시글이 삭제되었습니다."}, status=status.HTTP_200_OK)


class CommentApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, board_id, comment_id=None):
        info = {
            "user": request.user.id,
            "board": board_id,
            "comment": comment_id
        }
        comment = get_comment(info)
        return Response(comment, status=status.HTTP_200_OK)

    def post(self, request, board_id):
        request.data['user'] = request.user.id
        request.data['board'] = board_id
        comment = save_comment(**request.data)
        return Response(comment, status=status.HTTP_201_CREATED)

    def put(self, request, board_id, comment_id):
        request.data['user'] = request.user.id
        request.data['board'] = board_id
        request.data['comment'] = comment_id
        comment = edit_comment(**request.data)
        return Response(comment, status=status.HTTP_200_OK)

    def delete(self, request, board_id, comment_id):
        if delete_comment(board_id, comment_id):
            return Response({"msg": "댓글이 삭제되었습니다."}, status=status.HTTP_200_OK)


class LikeApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        return Response({"msg": "post method"})

    def delete(self, request):
        return Response({"msg": "delete method"})