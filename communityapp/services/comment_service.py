from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
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
        board = Board.objects.get(Q(category__kind__contains=data['category']) & Q(id=data['board']))
        comment_serializer = CommentSerializer(data=data)
        comment_serializer.is_valid(raise_exception=True)
        comment_serializer.save()
        return comment_serializer.data

    except ObjectDoesNotExist:
        response = {
            "detail": "해당 게시글이 존재하지 않습니다.",
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)


def edit_comment(**data):
    try:
        board = Board.objects.get(id=data['board'])
        comment = Comment.objects.get(board_id=data['board'], user_id=data['user'])
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


def delete_comment(comment_id):
    try:
        target_comment = Comment.objects.get(id=comment_id)
        target_comment.delete()
        return True

    except Comment.DoesNotExist:
        response = {
            "detail": "해당 댓글이 존재하지 않습니다.",
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)
