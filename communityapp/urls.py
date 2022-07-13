from django.urls import path

from communityapp import views

urlpatterns = [
    path('category/', views.BoardCategoryApiView.as_view()),
    path('category/<category_id>/', views.BoardCategoryApiView.as_view()),

    path('<int:category_id>/board/', views.BoardApiView.as_view()),
    path('<int:category_id>/board/<int:board_id>/', views.BoardApiView.as_view()),
    path('board/', views.BoardApiView.as_view())
]