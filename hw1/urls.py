from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginTask3, name="loginTask3"),
    path('home/', views.home, name="home"),
    path('logout/', views.logoutUser, name="logout"),
]
