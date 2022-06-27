from django.core.exceptions import ObjectDoesNotExist

from productapp.models import Product
from productapp.serializers import ProductSerializer


def get_product(product_id=None):
    if product_id:
        try:
            product = Product.objects.get(id=product_id)
            product_serializer = ProductSerializer(product).data
            return product_serializer
        except ObjectDoesNotExist:
            return False
    else:
        try:
            product = Product.objects.get(id=product_id)
            product_serializer = ProductSerializer(product).data
            return product_serializer
        except ObjectDoesNotExist:
            return False
