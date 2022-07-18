from django.urls import path

from communityapp import views

urlpatterns = [
    path('category/', views.BoardCategoryApiView.as_view()),
    path('category/<category_id>/', views.BoardCategoryApiView.as_view()),

    # 댓글 조회, 생성, 수정, 삭제
    path('comment/', views.CommentApiView.as_view()),
    path('comment/<int:board_id>/', views.CommentApiView.as_view()),
    path('comment/<int:board_id>/<int:comment_id>/', views.CommentApiView.as_view()),

    # 게시글 생성
    path('board/', views.BoardApiView.as_view()),
    # 게시글 수정, 삭제
    path('board/<int:board_id>/', views.BoardApiView.as_view()),

    # 게시글 좋아요
    path('board/like/'),

    # 카테고리별 게시글 조회
    path('<str:category_kind>/', views.BoardApiView.as_view()),
    path('<str:category_kind>/<int:board_id>/', views.BoardApiView.as_view()),
]
