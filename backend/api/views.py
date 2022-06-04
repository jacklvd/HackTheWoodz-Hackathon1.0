from rest_framework.response import Response
from rest_framework.decorators import api_view

# for testing purpose
@api_view(['GET'])
def getData(request):
    person = {'name':'Jacky', 'age':'20','music':'lofi'}
    return Response(person)

@api_view(['POST'])
def addData(request):
    person = {'name':'Jacky', 'age':'20','music':'pop'}
    return Response(person)