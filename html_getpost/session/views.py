from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.
def set_session(request):
    request.session['username']='001trijal'
    request.session['lastname']='luha'
    request.session.set_expiry(20)
    return HttpResponse('Session is set')

def get_session(request):
    username=request.session.get('username')
    lastname=request.session.get('lastname')

    print(username,lastname)

    return HttpResponse(f"get session {lastname} and {username} executed at {strtime}")

def del_user(request):
    del request.session['username']
    return HttpResponse('Username deleted')

def del_session(request):
    request.session.flush()
    return HttpResponse("Session flushed successfully")

def check_session(request):
    a=request.session.get_expiry_age()
    b=request.session.get_expiry_date()
    c=request.session.get_session_cookie_age()
    return HttpResponse(f"Session age left: {a}<br> Session will expire on: {b}<br>Session cookie age set: {c}")

def rem_expired(request):
    request.session.clear_expired()
    return HttpResponse("All expired sessions removed")