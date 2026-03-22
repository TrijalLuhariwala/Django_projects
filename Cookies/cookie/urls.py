from django.urls import path
from . import views

urlpatterns=[
    path('setcook/',views.set_cookies,name='setcook'),
    path('getcook/',views.get_cookies,name='getcook'),
    path('delcook/',views.del_cookies,name='delcook'),
    
]