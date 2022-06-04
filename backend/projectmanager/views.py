from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
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
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)