from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Employee
import json
# Create your views here.
def create_employee(request):
    if request.method=="POST":
        Employee.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            email=request.POST['email']
        )
        return redirect('employee_list')
    return render(request,'create.html')

def employee_list(request):
    employees=Employee.objects.all()
    return render(request,'list.html',{'employees':employees})

def update_employee(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=="POST":
        emp.name=request.POST['name']
        emp.age=request.POST['age']
        emp.email=request.POST['email']
        emp.save()
        return redirect('employee_list')
    return render(request,'update.html',{'emp':emp})

def delete_employee(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=="POST":
        emp.delete()
        return redirect('employee_list')
    return render(request,'delete.html',{'emp':emp})


    
        