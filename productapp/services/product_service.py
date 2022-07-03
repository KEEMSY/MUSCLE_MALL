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
            product = Product.objects.all()
            product_serializer = ProductSerializer(product, many=True).data
            return product_serializer
        except ObjectDoesNotExist:
            return False


def save_product(**kwargs):
    productserializer = ProductSerializer(data=kwargs)
    productserializer.is_valid(raise_exception=True)
    productserializer.save()
    return productserializer.data


def edit_product(product_id, **kwargs):
    try:
        product = Product.objects.get(id=product_id)
        product_serializer = ProductSerializer(product, data=kwargs, partial=True)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return product_serializer.data

    except ObjectDoesNotExist:
        return False


def delete_product(user, product_id=None):
    if product_id:
        try:
            product = Product.objects.get(user=user, id=product_id)
            product.delete()
            return True
        except ObjectDoesNotExist:
            return False
    else:
        try:
            product = Product.objects.filter(user=user)
            product.delete()
            return True
        except ObjectDoesNotExist:
            return False
