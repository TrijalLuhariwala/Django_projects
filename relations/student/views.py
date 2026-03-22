from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, StudentProfile
# Create your views here.
@api_view(['POST'])
def create_student(request):
    data=request.data
    student=Student.objects.create(
        name=data.get('name'),
        age=data.get('age'),
        email=data.get('email')
    )
    StudentProfile.objects.create(
        student=student,
        bio=data.get('bio'),
        address=data.get('address')
    )
    return Response({"message": "Student Created Successfully"})


@api_view(['GET'])
def get_students(request):
    students=Student.objects.all()
    data = []
    for student in students:
        data.append({
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "email": student.email,
        "bio": student.studentprofile.bio,
        "address": student.studentprofile.
        address
        })
    return Response(data)

@api_view(['GET'])
def get_student(request,id):
    try:
        student=Student.objects.get(id=id)
    except:
        return Response({"message":"Error : Student not found"},status=404)
    data={
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "email": student.email,
        "bio": student.studentprofile.bio,
        "address": student.studentprofile.address
    }
    return Response(data)

@api_view(['PUT'])
def update_student(request,id):
    try:
        student=Student.objects.get(id=id)
    except:
        return Response({"message":"Error : Student not found"},status=404)
    data=request.data
    student.name=data.get('name',student.name)
    student.age=data.get('age',student.age)
    student.email=data.get('email',student.email)
    student.studentprofile.bio=data.get('bio',student.studentprofile.bio)
    student.studentprofile.address=data.get('address',student.studentprofile.address)
    student.save()
    student.studentprofile.save()

    return Response({"message": f"Student with id {student.id} Updated Successfully"})

@api_view(['PATCH'])
def patch_student(request,id):
    try:
        student=Student.objects.get(id=id)
    except:
        return Response({"message":"Error : Student not found"},status=404)
    data=request.data
    student.name=data.get('name',student.name)
    student.age=data.get('age',student.age)
    student.email=data.get('email',student.email)
    student.studentprofile.bio=data.get('bio',student.studentprofile.bio)
    student.studentprofile.address=data.get('address',student.studentprofile.address)
    student.save()
    student.studentprofile.save()
    return Response({"message": f"Student with id {student.id} Patched Successfully"})


@api_view(['DELETE'])
def delete_student(request,id):
    try:
        student=Student.objects.get(id=id)
    except:
        return Response({"message":"Error : Student not found"},status=404)
    name=student.name
    id=student.id
    student.delete()
    return Response({"message": f"Student with name:{name} and id : {id} Deleted Successfully"})