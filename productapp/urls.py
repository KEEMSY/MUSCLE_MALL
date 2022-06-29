from django.urls import path

from productapp import views

urlpatterns = [
    path('category/', views.ProductCategoryApiView.as_view()),
    path('category/<category_id>/', views.ProductCategoryApiView.as_view()),

    path('detail/', views.ProductDetailCategoryApiView.as_view()),
    path('detail/<detail_category>/', views.ProductDetailCategoryApiView.as_view()),
    path('detail/<detail_category>/<detail_category_id>/', views.ProductDetailCategoryApiView.as_view()),

    path('routine/', views.RoutineApiView.as_view()),
    path('routine/<routine_id>/', views.RoutineApiView.as_view()),

    path('challenge/', views.ChallengeApiView.as_view()),
    path('challenge/<challenge_id>/', views.ChallengeApiView.as_view()),

    path('', views.ProductApiView.as_view()),
    path('<product_id>/', views.ProductApiView.as_view()),

]