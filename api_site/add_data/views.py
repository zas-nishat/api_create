from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics,status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


class showUserLists (generics.ListAPIView ):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class createUserList (generics.ListCreateAPIView ):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def delete(self, request, *args, **kwargs):
        User.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class updateUserList(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"
    
class deleteUserList(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def get_users(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many = True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_users(request):
#     serializer = UserSerializer(data= request.data)
#     if UserSerializer.is_valid:
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)