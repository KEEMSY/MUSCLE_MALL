from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from productapp.models import ProductCategory
from productapp.serializers import ProductCategorySerializer
from productapp.services.product_category_service import get_product_category, save_product_category, \
    edit_product_category


class ProductCategoryApiView(APIView):
    def get(self, request, category_id=None):
        category = get_product_category(category_id)
        if category:
            return Response(category, status=status.HTTP_200_OK)
        return Response({'msg': "카테고리가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        product_category = save_product_category(**request.data)
        return Response(product_category, status=status.HTTP_201_CREATED)

    def put(self, request, category_id):
        product_category = edit_product_category(category_id, **request.data)
        if product_category:
            return Response(product_category, status=status.HTTP_201_CREATED)
        return Response({'msg': "카테고리가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        return Response({'msg': "delete method"})
