from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Subject
# Create your views here.

@api_view(['POST'])
def create_subjects(request):
    for data in request.data:
        sub=Subject.objects.create(
            code=data.get('code'),
            name=data.get('name')
        )

    return Response({"message" : "Subject(s) added Succesfully"})

@api_view(['POST'])
def create_students(request):
    for data in request.data:
        stud=Student.objects.create(
            name=data.get('name'),
            age=data.get('age')
        )
        subs=data.get('subjects',[])
        for sub in subs:
            stud.subjects.add(Subject.objects.get(id=sub))
    
        # subjects = Subject.objects.filter(id__in=subject_ids)
        # student.subjects.set(subjects)
        
    return Response({"message" : "Student(s) added Succesfully"})


@api_view(['GET'])
def get_subjects(request):
    subs=Subject.objects.all()
    data=[]
    for sub in subs:
        studs=[i.name for i in sub.students.all()]
        data.append({
            "Code" : sub.code,
            "Name" : sub.name,
            "Students_enrolled" : studs
        })
    return Response(data)

@api_view(['GET'])
def get_students(request):
    studs=Student.objects.all()
    data=[]
    for stud in studs:
        subs=[f"{i.code} : {i.name}" for i in stud.subjects.all()]
        data.append({
            "Id" : stud.id,
            "Name" : stud.name,
            "Age" : stud.age,
            "Subjects" : subs
        })
    return Response(data)

@api_view(['PATCH'])
def update_subject(request,id):
    data=request.data
    sub=Subject.objects.get(id=id)
    sub.code=data.get('code',sub.code)
    sub.name=data.get('name',sub.name)
    sub.save()
    return Response({"message" : "Subject updated successfully"})

@api_view(['PATCH'])
def update_student(request,id):
    data=request.data
    stud=Student.objects.get(id=id)
    stud.name=data.get('name',stud.name)
    stud.age=data.get('age',stud.age)
    subs=data.get('subjects',None)
    if subs!=None:
        subjects = Subject.objects.filter(id__in=subs)
        stud.subjects.set(subjects)
    stud.save()
    return Response({"message" : "Student updated successfully"})

    
@api_view(['DELETE','GET'])
def del_student(request,id):
    stud=Student.objects.get(id=id)
    nm=stud.name
    stud.delete()
    return Response({"message" : f"Student with name {nm} deleted successfully"})


@api_view(['DELETE','GET'])
def del_subject(request,id):
    sub=Subject.objects.get(id=id)
    nm=sub.name
    sub.delete()
    return Response({"message" : f"Subject with name {nm} deleted successfully"})
