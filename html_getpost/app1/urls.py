from django.urls import path
from . import views

urlpatterns=[
    path('create/',views.create_employee,name='create_employee'),
    path('employees/',views.employee_list,name='employee_list'),
    path('update/<int:id>',views.update_employee,name='update_employee'),
    path('delete/<int:id>',views.delete_employee,name='delete_employee'),
    #path('at_create/',views.at_create,name='at_create')
]