from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .forms import Signup
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def index(request):
    return render(request,'home/index.html')

def signup(request):
    if request.method=="POST":
        fm=Signup(request.POST)  
        if fm.is_valid():
            fm.save()
            fm = Signup()
            return render(request,'home/signup.html',{'form':fm})
        return render(request,'home/signup.html',{'form':fm})  
    else:    
        fm = Signup()
        return render(request,'home/signup.html',{'form':fm})

def userlogin(request):
    if request.method=="POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile')
    else:
        fm = AuthenticationForm()
    return render(request,'home/userlogin.html',{'form':fm})

def profile(request):
    return render(request,'home/profile.html')

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')