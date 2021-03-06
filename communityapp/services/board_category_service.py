from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

from MM.api_exception import GenericAPIException
from communityapp.models import BoardCategory
from communityapp.serializers import BoardCategorySerializer


def get_board_category(category_id=None):
    if category_id:
        try:
            category = BoardCategory.objects.get(id=category_id)
            category_serializer = BoardCategorySerializer(category).data
            return category_serializer
        except ObjectDoesNotExist:
            response = {
                "detail": "해당 카테고리가 존재하지 않습니다.",
            }
            raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)

    else:
        categories = BoardCategory.objects.all()
        if len(categories):
            categories_serializer = BoardCategorySerializer(categories, many=True).data
            return categories_serializer
        else:
            response = {
                "detail": "해당 카테고리가 존재하지 않습니다.",
            }
            raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)


def save_board_category(**data):
    board_category = BoardCategorySerializer(data=data)
    board_category.is_valid(raise_exception=True)
    board_category.save()
    return board_category.data


def edit_board_category(category_id, **data):
    try:
        category = BoardCategory.objects.get(id=category_id)
        board_category_serializer = BoardCategorySerializer(category, data=data, partial=True)
        board_category_serializer.is_valid(raise_exception=True)
        board_category_serializer.save()
        return board_category_serializer.data

    except ObjectDoesNotExist:
        response = {
            "detail": "해당 카테고리가 존재하지 않습니다.",
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)


def delete_board_category(category_id):
    try:
        category = BoardCategory.objects.get(id=category_id)
        category.delete()
        return True
    except ObjectDoesNotExist:
        response = {
            "detail": "해당 카테고리가 존재하지 않습니다.",
        }
        raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)

