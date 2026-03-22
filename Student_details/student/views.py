from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Student
import json
# Create your views here.
def create_student(request):
    if request.method=="POST":
        Student.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            email=request.POST['email'],
            number=request.POST['number'],
        )
        return redirect('student_list')
    return render(request,'create.html')

def student_list(request):
    students=Student.objects.all()
    return render(request,'list.html',{'students':students})

def update_student(request,id):
    stud=Student.objects.get(id=id)
    if request.method=="POST":
        stud.name=request.POST['name']
        stud.age=request.POST['age']
        stud.email=request.POST['email']
        stud.number=request.POST['number']
        stud.save()
        return redirect('student_list')
    return render(request,'update.html',{'stud':stud})

def delete_student(request,id):
    stud=Student.objects.get(id=id)
    if request.method=="POST":
        stud.delete()
        return redirect('student_list')
    return render(request,'delete.html',{'stud':stud})
