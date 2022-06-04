from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import Project
from .serializers import ProjectSerializer

from django.contrib.auth.models import User


"""
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    tools = models.TextField()
    description = models.TextField(blank=True, null=True)
"""

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=False, methods=['get'])
    def projects(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def create(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = Project()
            project.user = User.objects.get(pk=request.user.id)
            project.title = (serializer.validated_data['title'])
            project.tools = (serializer.validated_data['tools'])
            project.description = (serializer.validated_data['description'])
            project.save()
            return Response({'status':'new project created'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
