from django.urls import path
from . import views

urlpatterns=[
    path('create/',views.create_student,name='create'),
    path('gets/',views.get_students,name='gets'),
    path('get/<int:id>/',views.get_student,name='get'),
    path('update/<int:id>/',views.update_student,name='update'),
    path('patch/<int:id>/',views.patch_student,name='patch'),
    path('delete/<int:id>/',views.delete_student,name='delete'),
]