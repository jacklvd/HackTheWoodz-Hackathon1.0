from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import Project
from .serializers import ProjectSerializer

from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
import json

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
<<<<<<< HEAD
            project.user = User.objects.get(pk=1)
            project.title = (serializer.validated_data['title'])
            project.tools = (serializer.validated_data['tools'])
            project.description = (serializer.validated_data['description'])
=======
            #project.user = User.objects.get(pk=request.user.id)
            project.user = User.objects.get(pk=1) # for testing

            title_data = serializer.validated_data['title']

            already_exists = Project.objects.filter(title=title_data)
        # UNCOMMENT THIS ONCE DONE TESTING WITH POSTMAN
            if already_exists: # and (already_exists.user == request.user):
                return Response({"error":"project with that title already exists"})

            tools_data = serializer.validated_data['tools']
            description_data = serializer.validated_data['description']
            image_data = serializer.validated_data['images']

            if title_data == None or tools_data == None or description_data == None or image_data == None:
                return Response({"error":"required fields missing"})

            project.title = title_data
            project.tools = tools_data
            project.description = description_data
>>>>>>> 7696d1b52a33002026f0d67169cdc8e8adc61dbf
            project.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['patch'])
    def update(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data, partial=True)

        if serializer.is_valid():
                    # grab project by title
            if serializer.initial_data.get('title'):
                title_data = serializer.validated_data['title']
                project = get_object_or_404(Project, title=title_data)
            else:
                return Response({"error":"project not found"})

            #id is not passed in serializer due to being read only
            #project_id = (serializer.validated_data['id'])

        # UNCOMMENT THIS ONCE DONE TESTING WITH POSTMAN
            if project.user: # == request.user:

                # update anything that's changed been changed in request body

                if serializer.data.get('tools'):
                    project.tools = serializer.validated_data['tools']

                if serializer.data.get('description'):
                    project.description = serializer.validated_data['description']

                if serializer.data.get('images'):
                    project.images = serializer.validated_data['images']

                project.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_image(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            title_data = (serializer.validated_data['title'])
            project = get_object_or_404(Project, title=title_data)
            img = "/media/" + str(project.images)

            return Response({"images":img})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
