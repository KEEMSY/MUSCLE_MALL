from rest_framework import status
from rest_framework.exceptions import ValidationError

from MM.api_exception import GenericAPIException
from communityapp.models import BoardLike, Board
from communityapp.serializers import BoardLikeSerializer


def save_board_like(user_id, board_id):
    try:
        Board.objects.get(id=board_id)
        board_like = BoardLikeSerializer(data={
            "user": user_id,
            "board": board_id
        })
        board_like.is_valid(raise_exception=True)
        board_like.save()

        return board_like.data

    except Board.DoesNotExist:
        response = {
            "detail": "게시글이 존재하지 않습니다."
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)

    except ValidationError:
        response = {
            "detail": "좋아요는 게시글 당 한개만 가능합니다."
        }
        raise GenericAPIException(status_code=status.HTTP_400_BAD_REQUEST, detail=response)


def delete_board_like(user_id, board_id):
    try:
        board = Board.objects.get(id=board_id)
        BoardLike.objects.get(user_id=user_id, board_id=board_id).delete()
        return True

    except BoardLike.DoesNotExist:
        response = {
            "detail": "좋아요가 존재하지 않습니다."
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)

    except Board.DoesNotExist:
        response = {
            "detail": "게시글이 존재하지 않습니다."
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)
