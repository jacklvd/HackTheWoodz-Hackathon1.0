from django.urls import path
from .views import ProjectViewSet

urlpatterns = [
    path('projects/', ProjectViewSet.as_view({'get':'projects'})),
    path('create/', ProjectViewSet.as_view({'post':'create'})),
    path('update/', ProjectViewSet.as_view({'post':'update'})),
]

# name, job title, all images, project title, project desc
