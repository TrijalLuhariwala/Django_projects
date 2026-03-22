from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def set_cookies(request):
    response=HttpResponse('Set Cookies')
    response.set_cookie('name','trijal')
    response.set_cookie('last_name','luhariwala')
    
    return response

def get_cookies(request):
    name=request.COOKIES.get('name')
    lastname=request.COOKIES.get('last_name')
    
    return HttpResponse(f"Got cookies:<br>Name: {name}<br>Last Name: {lastname}")

def del_cookies(request):
    response=HttpResponse("Cookie deleted")
    response.delete_cookie('name')
    return response
    