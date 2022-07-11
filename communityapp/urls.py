from django.urls import path

from communityapp import views

urlpatterns = [
    path('category/', views.BoardCategoryApiView.as_view()),
]