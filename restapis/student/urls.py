from django.urls import path
from . import views

urlpatterns=[
    path('students/',views.get_students,name='students'),
    path('student/<int:id>',views.get_student,name='student'),
    path('create/',views.create_students,name='create'),
    path('update/<int:id>',views.update_student,name='update'),
    path('patch/<int:id>',views.patch_student,name='patch'),
    path('delete/<int:id>',views.delete_student,name='delete'),
]