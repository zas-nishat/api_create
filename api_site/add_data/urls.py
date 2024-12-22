from django.urls import path
from . import views


urlpatterns = [
    path('userlist/', views.createUserList.as_view() , name= "user-create-view"),
]
