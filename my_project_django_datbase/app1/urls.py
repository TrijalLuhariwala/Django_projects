from django.urls import path
from . import views

urlpatterns=[
    path('employees/',views.get_employees),
    path('newemp/',views.create_employee),
    path('employee/<int:id>',views.get_employee),
    path('update/<int:id>',views.update_employee),
    path('delete/<int:id>',views.delete_employee)
]