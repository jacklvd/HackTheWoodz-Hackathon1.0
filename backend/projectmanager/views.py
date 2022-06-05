#  django packages
from functools import partial
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, permissions
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

# project packages
from projectmanager.models import Project, User
from .serializers import ProjectSerializer, UserSerializer

# for testing purpose
# def get_base_url(request):
#     host = get_host(request)
#     if request.is_secure():
#         return '{0}{1}/{2}'.format('https://', host, 'url')
#     else:
#         return '{0}{1}/{2}'.format('http://', host, 'url')

# @api_view(['GET'])
# def getData(request):
#     person = Project.objects.all()
#     serializer = ProjectSerializer(person, many=True)
#     return Response(request, serializer.data)

# @api_view(['POST'])
# def addData(request):
#     serializer = ProjectSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(request, serializer.data)

# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # check if the user is exist
#         try:
#             user = User.objects.get(username=username)
#         except:
#             messages.error(request, 'User does not exit')
            
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request,user) #add database of user
#             return redirect('home') # return the user to homepage for now just placeholder
#         else:
#             messages.error(request, 'Username or Password does not exit')    
    
#     return Response(username) #placeholder for now


# """
#     user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
#     title = models.CharField(max_length=25)
#     tools = models.TextField()
#     description = models.TextField(blank=True, null=True)
# """

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

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    # this one for us to check the data, not really an endpoint tho
    @action(detail=False)
    def recent_users(self, request):
        recent_users = User.objects.all().order_by('-last_login')

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)
    
    # endpoint for login page    
    # @action(detail=True, methods=['post'])
    # def loginPage(self, request):
    #     # serializer = ProjectSerializer(data=request.data, partial=True)
    #     user = User()
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     # check if the user is exist
    #     try:
    #         user = User.objects.get(username=username)
    #     except:
    #         messages.error(request, 'User does not exit')
            
    #     userAu = authenticate(request, username=username, password=password)
        
    #     if userAu is not None:
    #         login(request,userAu) #add database of user
    #         return redirect('home') # return the user to homepage for now just placeholder
    #     else:
    #         messages.error(request, 'Username or Password does not exit')    
    #     # context = {}
    #     return Response(userAu, status=status.HTTP_202_ACCEPTED) #placeholder for now

    # @csrf_exempt
    # @api_view(["POST"])
    # @permission_classes((AllowAny,))
    # def login(self, request):
    #     username = request.data.get("username")
    #     password = request.data.get("password")
    #     if username is None or password is None:
    #         return Response({'error': 'Please provide both username and password'},
    #                         status=HTTP_400_BAD_REQUEST)
    #     user = authenticate(username=username, password=password)
    #     if not user:
    #         return Response({'error': 'Invalid Credentials'},
    #                         status=HTTP_404_NOT_FOUND)
    #     token, _ = Token.objects.get_or_create(user=user)
    #     return Response({'token': token.key},
    #                     status=HTTP_200_OK)

    
    # a get action I guess
    def logoutUser(request):
        logout(request)
        return redirect('home') # placeholder for the homepage/login page
    
    