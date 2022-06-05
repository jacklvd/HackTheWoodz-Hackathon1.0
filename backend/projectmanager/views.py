from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import Project
from .serializers import ProjectSerializer

from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

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
            #project.user = User.objects.get(pk=request.user.id)
            project.user = User.objects.get(pk=1) # for testing
            project.title = (serializer.validated_data['title'])
            project.tools = (serializer.validated_data['tools'])
            project.description = (serializer.validated_data['description'])
            project.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['patch'])
    def update(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            if request.user.id == serializer.validated_data['user']:
                t = (serializer.validated_data['title'])
                project = get_object_or_404(Project, title=t)
                project.images = (serializer.validated_data['images'])
                project.save()

                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
