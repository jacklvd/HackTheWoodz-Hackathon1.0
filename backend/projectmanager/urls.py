from django import urls
from django.urls import path
from .views import ProjectViewSet
from rest_framework.authtoken import views

urlpatterns = [
    path('projects/', ProjectViewSet.as_view({'get':'projects'})),
    path('create/', ProjectViewSet.as_view({'post':'create'})),
    path('update/', ProjectViewSet.as_view({'post':'update'})),
    # path('login/', ProjectViewSet.as_view({'post':'loginPage'})),
    path('logout/', ProjectViewSet.logoutUser, name='logout'),
    path('password/', ProjectViewSet.as_view({'post':'set_password'})),
]

# urlpatterns += [
#     urls(r'^api-token-auth/', views.obtain_auth_token)
# ]