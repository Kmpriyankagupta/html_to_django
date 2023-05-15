from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.UserRegister, name= "signup"),
    path('loginpage/', views.LoginPage,name='loginpage'),
    path('login/', views.Login, name='login'),
    path('login/logout/', views.logout_view, name='logout')
]