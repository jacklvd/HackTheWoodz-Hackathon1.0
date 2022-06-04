from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from projectmanager import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projectmanager/', include(urls)),
    #path('auth-api/', include('rest_framework.urls')),
]
