from django.urls import path

from userapp import views

urlpatterns =[
    path('', views.UserApiView.as_view()),
    path('login/', views.UserView.as_view()),
    path('logout/', views.UserView.as_view()),

    path('<user_id>/', views.UserApiView.as_view()),

]