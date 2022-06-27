from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from productapp.serializers import ProductCategorySerializer
from productapp.services.product_category_service import get_product_category


class ProductCategoryApiView(APIView):
    def get(self, request, category_id=None):
        category = get_product_category(category_id)
        if category:
            return Response(category, status=status.HTTP_200_OK)
        return Response({'msg': "카테고리가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        return Response({'msg': "post method"})

    def put(self, request):
        return Response({'msg': "put method"})

    def delete(self, request):
        return Response({'msg': "delete method"})
