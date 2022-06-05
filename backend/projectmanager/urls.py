from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData, name="get"),
    path('add/', views.addData, name="add"),
    path('login/', views.loginPage, name='login')
]
