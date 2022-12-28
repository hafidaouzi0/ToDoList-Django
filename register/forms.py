from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        #this makes us show the fields in the order we want
        fields=["username","email","password1","password2"]
