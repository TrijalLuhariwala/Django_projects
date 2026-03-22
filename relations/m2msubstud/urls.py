from django.urls import path
from . import views

urlpatterns=[
    path('cstuds/',views.create_students,name="cstuds"),
    path('csubs/',views.create_subjects,name="csubs"),
    
    path('gsubs/',views.get_subjects,name="gsubs"),
    path('gstuds/',views.get_students,name="gstuds"),

    path('ustud/<int:id>/',views.update_student,name='ustud'),
    path('usub/<int:id>/',views.update_subject,name='usub'),

    path('dstud/<int:id>/',views.del_student,name='dstud'),
    path('dsub/<int:id>/',views.del_subject,name='dsub')
]