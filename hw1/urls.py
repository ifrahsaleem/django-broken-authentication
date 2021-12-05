from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginTask3),
    path('', views.loginTask3, name="loginTask3"),
    path('home/', views.home, name="home"),
    path('logout/', views.logoutUser, name="logout"),
    path('register1/', views.registerTask1, name='registerTask1'),
    path('register2/', views.registerTask2, name="registerTask2"),
]
