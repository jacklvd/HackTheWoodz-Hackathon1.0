#  django packages
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, permissions
from django.contrib.auth.models import User
from django.contrib import messages

# project packages
from projectmanager.models import Project
from .serializers import ProjectSerializer

# for testing purpose
# def get_base_url(request):
#     host = get_host(request)
#     if request.is_secure():
#         return '{0}{1}/{2}'.format('https://', host, 'url')
#     else:
#         return '{0}{1}/{2}'.format('http://', host, 'url')

@api_view(['GET'])
def getData(request):
    person = Project.objects.all()
    serializer = ProjectSerializer(person, many=True)
    return Response(request, serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(request, serializer.data)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if the user is exist
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exit')
    return Response(username)


# """
#     user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
#     title = models.CharField(max_length=25)
#     tools = models.TextField()
#     description = models.TextField(blank=True, null=True)
# """

# class ProjectViewSet(ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

#     @action(detail=False, methods=['get'])
#     def projects(self, request):
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     @action(detail=True, methods=['post'])
#     def create(self, request, *args, **kwargs):
#         serializer = ProjectSerializer(data=request.data)
#         if serializer.is_valid():
#             project = Project()
#             project.user = User.objects.get(pk=request.user.id)
#             project.title = (serializer.validated_data['title'])
#             project.tools = (serializer.validated_data['tools'])
#             project.description = (serializer.validated_data['description'])
#             project.save()
#             return Response({'status':'new project created'})
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)