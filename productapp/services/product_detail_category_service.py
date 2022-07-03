from django.core.exceptions import ObjectDoesNotExist

from productapp.models import ProductDetailCategory
from productapp.serializers import ProductDetailCategorySerializer


def get_product_detail_category(detail_category=None, detail_category_id=None):
    if detail_category:
        try:
            categories = ProductDetailCategory.objects.filter(category_id=detail_category)
            if detail_category_id:
                try:
                    category = categories.get(id=detail_category_id)
                    category_serializer = ProductDetailCategorySerializer(category).data
                    return category_serializer
                except ObjectDoesNotExist:
                    return False

            categories_serializer = ProductDetailCategorySerializer(categories, many=True).data
            return categories_serializer

        except ObjectDoesNotExist:
            return False
    else:
        try:
            categories = ProductDetailCategory.objects.all()
            categories_serializer = ProductDetailCategorySerializer(categories, many=True).data
            return categories_serializer
        except ObjectDoesNotExist:
            return False


def save_product_detail_category(**kwargs):
    product_detail_category_serializer = ProductDetailCategorySerializer(data=kwargs)
    product_detail_category_serializer.is_valid(raise_exception=True)
    product_detail_category_serializer.save()
    return product_detail_category_serializer.data


def edit_product_detail_category(detail_category, detail_category_id, **kwargs):
    try:
        category = ProductDetailCategory.objects.get(id=detail_category_id, category_id=detail_category)
        product_detail_category_serializer = ProductDetailCategorySerializer(category, data=kwargs, partial=True)
        product_detail_category_serializer.is_valid(raise_exception=True)
        product_detail_category_serializer.save()
        return product_detail_category_serializer.data

    except ObjectDoesNotExist:
        return False


def delete_product_delete_category(detail_category, detail_category_id):
    try:
        category = ProductDetailCategory.objects.get(id=detail_category_id, category_id=detail_category)
        category.delete()
        return True
    except ObjectDoesNotExist:
        return False
