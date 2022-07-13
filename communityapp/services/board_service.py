from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import status

from MM.api_exception import GenericAPIException
from communityapp.models import Board
from communityapp.serializers import BoardSerializer


def get_board(category_kind=None, board_id=None):
    if category_kind:
        boards_in_category = Board.objects.filter(
            Q(category__kind__icontains=category_kind)
        )
        if board_id:
            try:
                boards_in_category = boards_in_category.get(id=board_id)
                board_serializer = BoardSerializer(boards_in_category)
                return board_serializer.data

            except ObjectDoesNotExist:
                response = {
                    "detail": "해당 게시글이 존재하지 않습니다.",
                }
                raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)

        board_serializer = BoardSerializer(boards_in_category, many=True)
        return board_serializer.data

    all_boards = Board.objects.all()
    board_serializer = BoardSerializer(all_boards, many=True)

    return board_serializer.data


def save_board(**data):
    board_serializer = BoardSerializer(data=data)
    board_serializer.is_valid(raise_exception=True)
    board_serializer.save()
    return board_serializer.data


def edit_board(board_id, **data):
    try:
        board = Board.objects.get(id=board_id, user_id=data['user'])
        board_serializer = BoardSerializer(board, data=data, partial=True)
        board_serializer.is_valid(raise_exception=True)
        board_serializer.save()
        return board_serializer.data

    except ObjectDoesNotExist:
        response = {
            "detail": "해당 게시글이 존재하지 않습니다.",
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)


