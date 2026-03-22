from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django")

def index(request):
    return render(request,'index.html')

def index2(request):
    return render(request,'index2.html')

def index3(request):
    return render(request,'index3.html')

def index0(request):
    return render(request,'index0.html')