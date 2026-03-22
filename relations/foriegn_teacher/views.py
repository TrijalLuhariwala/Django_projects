from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Teacher
# Create your views here.

@api_view(['POST'])
def create_teacher(request):
    data=request.data
    teacher=Teacher.objects.create(
        name=data.get('name'),
        subject=data.get('subject')
    )
    return Response({"message": "Teacher Created Successfully"})

@api_view(['POST'])
def create_student(request):
    data=request.data

    try:
        teach=Teacher.objects.get(id=data.get('t_id'))
    except:
        return Response({"message":"Error : Student not found"},status=404)
    
    student=Student.objects.create(
        name=data.get('name'),
        age=data.get('age'),
        teacher=teach
    )
    return Response({"message": "Student Created Successfully"})


@api_view(['GET'])
def get_students(request):
    students=Student.objects.all()
    data=[]
    for student in students:
        data.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "teacher_name": student.teacher.name,
            "subject": student.teacher.subject
            })
    return Response(data)

@api_view(['GET'])
def get_teachers(request):
    teachers=Teacher.objects.all()
    data=[]
    for teach in teachers:
        stud_data=[]
        students=teach.students.all()
        for stud in students:
            stud_data.append(stud.name)
        data.append({
            "id": teach.id,
            "name": teach.name,
            "subject": teach.subject,
            "no_students": len(stud_data),
            "students": stud_data
            })
    return Response(data)

@api_view(['GET'])
def get_student(request,id):
    student=Student.objects.get(id=id)
    data={
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "teacher_name": student.teacher.name,
        "subject": student.teacher.subject
        }
    return Response(data)


@api_view(['GET'])
def get_teacher(request,id):
    teacher=Teacher.objects.get(id=id)
    stud_data=[i.name for i in teacher.students.all()]
    data={
        "id": teacher.id,
        "name": teacher.name,
        "subject": teacher.subject,
        "no_students": len(stud_data),
        "students": stud_data
        }
    return Response(data)


