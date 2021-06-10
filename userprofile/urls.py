from django.urls import path
from .views import *


urlpatterns = [
    path('profile/',profile_page,name='profile'),
    path('register/',UserProfileRegister,name='register'),
    path('login/',login_page,name='login'),
]