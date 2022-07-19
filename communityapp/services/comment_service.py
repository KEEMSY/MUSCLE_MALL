from rest_framework import status

from MM.api_exception import GenericAPIException
from communityapp.models import Comment, Board
from communityapp.serializers import CommentSerializer


def get_comment(info):
    if info['board']:
        try:
            board = Board.objects.get(id=info['board'])
            if info['comment']:
                target_comment = Comment.objects.get(id=info['comment'], board_id=info['board'])
                comment_serializer = CommentSerializer(target_comment)
                return comment_serializer.data

            comments_serializer = CommentSerializer(Comment.objects.filter(board_id=info['board']), many=True)
            return comments_serializer.data

        except Comment.DoesNotExist:
            response = {
                "detail": "댓글이 존재하지 않습니다.",
            }
            raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)

        except Board.DoesNotExist:
            response = {
                "detail": "해당 게시글이 존재하지 않습니다.",
            }
            raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)


def save_comment(**data):
    try:
        board = Board.objects.get(id=data['board'])
        comment_serializer = CommentSerializer(data=data)
        comment_serializer.is_valid(raise_exception=True)
        comment_serializer.save()
        return comment_serializer.data

    except Board.DoesNotExist:
        response = {
            "detail": "게시글이 존재하지 않습니다.",
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)


def edit_comment(**data):
    try:
        board = Board.objects.get(id=data['board'])
        comment = Comment.objects.get(id=data['comment'], user_id=data['user'])
        comment_serializer = CommentSerializer(comment, data=data, partial=True)
        comment_serializer.is_valid(raise_exception=True)
        comment_serializer.save()
        return comment_serializer.data

    except Board.DoesNotExist:
        response = {
            "detail": "해당 게시글이 존재하지 않습니다."
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)

    except Comment.DoesNotExist:
        response = {
            "detail": "해당 댓글이 존재하지 않습니다.",
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)


def delete_comment(board_id, comment_id):
    try:
        board = Board.objects.get(id=board_id)
        target_comment = Comment.objects.get(id=comment_id)
        target_comment.delete()
        return True

    except Board.DoesNotExist:
        response = {
            "detail": "게시글이 존재하지 않습니다.",
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)

    except Comment.DoesNotExist:
        response = {
            "detail": "해당 댓글이 존재하지 않습니다.",
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)
