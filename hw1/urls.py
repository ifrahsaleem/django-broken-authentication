from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginTask3),
    path('register1/', views.registerTask1, name='registerTask1')
]
