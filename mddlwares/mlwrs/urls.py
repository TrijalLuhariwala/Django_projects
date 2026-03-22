from django.urls import path
from . import views
urlpatterns=[
    path('fmw/',views.fmw_view,name='fmw'),
]