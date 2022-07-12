from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from communityapp.services.board_service import get_board_category


class BoardCategoryApiView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, category_id=None):
        category = get_board_category(category_id)
        return Response(category, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({'msg': 'post method'})

    def put(self, request):
        return Response({'msg': 'put method'})

    def delete(self, request):
        return Response({'msg': 'delete method'})
