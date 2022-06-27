from django.core.exceptions import ObjectDoesNotExist

from productapp.models import ProductCategory
from productapp.serializers import ProductCategorySerializer


def get_product_category(category_id=None):
    if category_id:
        try:
            category = ProductCategory.objects.get(id=category_id)
            category_serializer = ProductCategorySerializer(category).data
            return category_serializer
        except ObjectDoesNotExist:
            return False
    else:
        try:
            categories = ProductCategory.objects.all()
            categories_serializer = ProductCategorySerializer(categories, many=True).data
            return categories_serializer
        except ObjectDoesNotExist:
            return False


def save_product_category(**kwargs):
    product_category_serializer = ProductCategorySerializer(data=kwargs)
    product_category_serializer.is_valid(raise_exception=True)
    product_category_serializer.save()
    return product_category_serializer.data


def edit_product_category(category_id, **kwargs):
    try:
        category = ProductCategory.objects.get(id=category_id)
        product_category_serializer = ProductCategorySerializer(category, data=kwargs, partial=True)
        product_category_serializer.is_valid(raise_exception=True)
        product_category_serializer.save()
        return product_category_serializer.data

    except ObjectDoesNotExist:
        return False