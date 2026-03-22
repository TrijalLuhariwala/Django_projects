from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
import json
# Create your views here.
def get_employees(request):
    if request.method=="GET":
        employees=list(Employee.objects.values())
        return JsonResponse(employees,safe=False)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def create_employee(request):
    if request.method=="POST":
        data=json.loads(request.body)
        c=0
        for i in data:
            c+=1
            emp=Employee.objects.create(
                name=i['name'],
                age=i['age'],
                email=i['email']
            )
        return JsonResponse({'message':f"{c} Employee created"})

def get_employee(request,id):
    if request.method=="GET":
        emp=Employee.objects.get(id=id)

    data={
        "id":emp.id,
        "name":emp.name,
        "age": emp.age,
        "email": emp.email
    }
    return JsonResponse(data)

@csrf_exempt
def update_employee(request,id):
    if request.method=="POST" or request.method=="PUT":
        data=json.loads(request.body)
        emp=Employee.objects.get(id=id)
        emp.name=data.get("name",emp.name)
        emp.age=data.get("age",emp.age)
        emp.email=data.get("email",emp.email)
        emp.save()
        
        return JsonResponse({'message': f"Employee with id: {emp.id} updated"})

@csrf_exempt
def delete_employee(request,id):
    if request.method=="DELETE":
        emp=Employee.objects.get(id=id)
        emp.delete()

        return JsonResponse({'message': f"Employee with id {id} deleted"})
        