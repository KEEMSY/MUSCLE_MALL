from django.db.models import Q

from communityapp.models import Board
from communityapp.serializers import BoardSerializer


def get_board(category_id=None, board_id=None):
    if category_id:
        boards_in_category = Board.objects.filter(
            Q(category=category_id)
        )
        if board_id:
            boards_in_category = boards_in_category.get(id=board_id)
            board_serializer = BoardSerializer(boards_in_category)
            return board_serializer.data

        board_serializer = BoardSerializer(boards_in_category, many=True)
        return board_serializer.data

    all_boards = Board.objects.all()
    return all_boards
