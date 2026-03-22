from django.shortcuts import render

from django.http import HttpResponse

def get_blog(request):
    return HttpResponse("Hey this is my blog")

# Create your views here.
