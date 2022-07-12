from django.urls import path

from communityapp import views

urlpatterns = [
    path('category/', views.BoardCategoryApiView.as_view()),
    path('category/<category_id>/', views.BoardCategoryApiView.as_view()),
]