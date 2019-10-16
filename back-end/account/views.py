from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, BabySerializer

# Create your views here.

@api_view(["POST"])
def signup(request):
    
    serializer = UserSerializer(data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
    
    


def login(request):
    pass


def logout(request):
    pass

