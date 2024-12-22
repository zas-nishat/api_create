from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.createUserList.as_view() , name= "user-create-view"),
    path('users/<int:pk>/', views.retrieveUpdateDestroyUserList.as_view(), name= 'update')  
]
