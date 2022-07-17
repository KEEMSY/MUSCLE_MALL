from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import status

from MM.api_exception import GenericAPIException
from communityapp.models import Comment, Board
from communityapp.serializers import CommentSerializer


def get_comment(user_id, comment_id=None):
    comments = Comment.objects.filter(user_id=user_id)
    if comment_id:
        try:
            target_comment = comments.get(id=comment_id)
            comment_serializer = CommentSerializer(target_comment)
            return comment_serializer.data
        except ObjectDoesNotExist:
            response = {
                "detail": "해당 댓글이 존재하지 않습니다.",
            }
            raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)

    comments_serializer = CommentSerializer(comments, many=True)
    return comments_serializer.data


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
        comment = Comment.objects.get(id=data['board'], user_id=data['user'])
        comment_serializer = CommentSerializer(comment, data=data, partial=True)
        comment_serializer.is_valid(raise_exception=True)
        comment_serializer.save()
        return comment_serializer.data

    except ObjectDoesNotExist:
        response = {
            "detail": "해당 게시글/댓글이 존재하지 않습니다.",
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)
