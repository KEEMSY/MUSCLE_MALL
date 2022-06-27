from django.urls import path

from productapp import views

urlpatterns = [
    path('category/', views.ProductCategoryApiView.as_view()),
    path('category/<category_id>/', views.ProductCategoryApiView.as_view()),
    path('routine/', views.RoutineApiView.as_view()),
    path('routine/<routine_id>', views.RoutineApiView.as_view()),
    path('', views.ProductApiView.as_view()),
    path('<product_id>/', views.ProductApiView.as_view()),

]