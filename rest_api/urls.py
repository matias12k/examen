from django.urls import path
from rest_api.viewslogin import login

urlpatterns =[
   
    path('login/',login,name="login"),
]