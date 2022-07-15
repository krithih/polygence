from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Signup(UserCreationForm):
    password2 = forms.CharField(label="Confirm password:",widget=forms.PasswordInput)
    password1 = forms.CharField(label="Password:",widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
