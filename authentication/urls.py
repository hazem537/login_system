from django.urls import path 
from.views import  login,signup,main,logout
urlpatterns = [
path('',main ,name="main"),
path('login/',login ,name="login"),
path('signup/',signup ,name="signup"),
path('logout/',logout ,name="logout"),
]
