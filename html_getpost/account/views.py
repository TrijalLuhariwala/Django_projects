from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User

def signup_view(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})

def login_view(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            login(request,form.user)
            return redirect('home')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def home(request):
    return render(request,'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')
    

# Create your views here.
