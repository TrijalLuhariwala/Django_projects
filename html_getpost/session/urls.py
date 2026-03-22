from django.urls import path
from . import views
urlpatterns=[
    path('set/',views.set_session,name='set'),
    path('get/',views.get_session,name='get'),
    path('delu/',views.del_user,name='delu'),
    path('dels/',views.del_session,name='dels'),
    path('age/',views.check_session,name='age'),
    path('rem/',views.rem_expired,name='rem'),
    
]