from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile

class UserprofileForm(UserCreationForm):
    name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','name','age','email','password1','password2']