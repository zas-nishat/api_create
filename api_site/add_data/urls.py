from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.showUserLists.as_view() , name= "create-user"),    
    path('create/', views.createUserList.as_view() , name= "create-user"),
    path('update/<int:pk>/', views.updateUserList.as_view(), name= 'update') ,
    path('delete/<int:pk>/', views.deleteUserList.as_view(), name= 'delete')  
]


# urlpatterns = [
#     path('users/', get_users , name= "users"),
#     path('users/create/', create_users , name= "new_users"),
# ]