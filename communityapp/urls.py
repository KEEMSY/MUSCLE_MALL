from django.urls import path

from communityapp import views

urlpatterns = [
    path('category/', views.BoardCategoryApiView.as_view()),
    path('category/<category_id>/', views.BoardCategoryApiView.as_view()),

    # 카테고리별 게시글 조회
    path('<str:category_kind>/board/', views.BoardApiView.as_view()),
    path('<str:category_kind>/board/<int:board_id>/', views.BoardApiView.as_view()),
    # 게시글 생성
    path('board/', views.BoardApiView.as_view()),
]