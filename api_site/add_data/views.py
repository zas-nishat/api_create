from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics,status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer



## Show All Users List
class showUserLists (generics.ListAPIView ):
    queryset = User.objects.all()
    serializer_class = UserSerializer

## Create New User
class createUserList (generics.ListCreateAPIView ):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def delete(self, request, *args, **kwargs):
        User.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

## Update User Details
class updateUserList(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

## Delete User
class deleteUserList(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
