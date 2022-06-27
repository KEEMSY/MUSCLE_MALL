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
