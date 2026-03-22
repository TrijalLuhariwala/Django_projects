from django.urls import path
from . import views

urlpatterns=[
    path('create/',views.create_student,name='create_student'),
    path('students/',views.student_list,name='student_list'),
    path('update/<int:id>',views.update_student,name='update_student'),
    path('delete/<int:id>',views.delete_student,name='delete_student'),
    #path('at_create/',views.at_create,name='at_create')
]