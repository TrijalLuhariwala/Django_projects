from django.urls import path
from . import views

urlpatterns=[path('',views.home, name='home'),
            path('index/',views.index,name='index'),
            path('index2/',views.index2,name='index2'),
            path('index3/',views.index3,name='index3'),
            path('index0/',views.index0,name='index0')]
