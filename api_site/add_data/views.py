from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class createUserList (generics.ListCreateAPIView ):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class retrieveUpdateDestroyUserList(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"