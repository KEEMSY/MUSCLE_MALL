from rest_framework import status
from rest_framework.exceptions import ValidationError

from MM.api_exception import GenericAPIException
from communityapp.models import Board, BoardBookmark
from communityapp.serializers import BookmarkBoardSerializer


def save_board_bookmark(user_id, board_id):
    try:
        Board.objects.get(id=board_id)
        board_bookmark = BookmarkBoardSerializer(data={
            "user": user_id,
            "board": board_id
        })
        board_bookmark.is_valid(raise_exception=True)
        board_bookmark.save()

        return board_bookmark.data

    except Board.DoesNotExist:
        response = {
            "detail": "게시글이 존재하지 않습니다."
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)

    except ValidationError:
        response = {
            "detail": "북마크는 게시글 당 한개만 가능합니다."
        }
        raise GenericAPIException(status_code=status.HTTP_400_BAD_REQUEST, detail=response)


def delete_board_bookmark(user_id, board_id):
    try:
        board = Board.objects.get(id=board_id)
        BoardBookmark.objects.get(user_id=user_id, board_id=board_id).delete()
        return True

    except BoardBookmark.DoesNotExist:
        response = {
            "detail": "북마크가 존재하지 않습니다."
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)

    except Board.DoesNotExist:
        response = {
            "detail": "게시글이 존재하지 않습니다."
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)
