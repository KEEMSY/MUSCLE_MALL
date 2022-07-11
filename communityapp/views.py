from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class BoardCategoryApiView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        return Response({'msg': 'get method'})

    def post(self, request):
        return Response({'msg': 'post method'})

    def put(self, request):
        return Response({'msg': 'put method'})

    def delete(self, request):
        return Response({'msg': 'delete method'})
