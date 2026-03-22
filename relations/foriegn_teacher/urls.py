from django.urls import path
from . import views

urlpatterns=[
    path('ct/',views.create_teacher,name="ct"),
    path('cs/',views.create_student,name="cs"),
    
    path('gts/',views.get_teachers,name="gts"),
    path('gss/',views.get_students,name="gss"),
    
    path('gt/<int:id>',views.get_teacher,name="gt"),
    path('gs/<int:id>',views.get_student,name="gs"),
]