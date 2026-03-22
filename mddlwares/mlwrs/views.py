from django.shortcuts import render
from django.http import HttpResponse

def fmw_view(request):
    print("Hiii from views")
    return HttpResponse("Hii")
# Create your views here.
