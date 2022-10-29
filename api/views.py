from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    data = {"slackUsername": "alaokolapo7", 
     "backend": True, "age": 21, 
     "bio": "I am an up and coming Django backend developer."}
    return Response(data)