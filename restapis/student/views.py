from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def get_students(request):
    students=Student.objects.all()
    serializer=StudentSerializer(students,many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def get_student(request,id):
    student=Student.objects.get(id=id)
    serializer=StudentSerializer(student)
    return Response(serializer.data)

@api_view(['POST'])
def create_students(request):
    serializer = StudentSerializer(data=request.data,many=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=200 )#status=status.HTTP_201_CREATED

    return Response(serializer.errors, status=400)#status=status.HTTP_400_BAD_REQUEST

@api_view(['PUT'])
def update_student(request,id):
    stud=Student.objects.get(id=id)
    serializer = StudentSerializer(stud,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=200 )#status=status.HTTP_201_CREATED

    return Response(serializer.errors, status=400)#status=status.HTTP_400_BAD_REQUEST


@api_view(['PATCH'])
def patch_student(request,id):
    stud=Student.objects.get(id=id)
    serializer = StudentSerializer(stud,data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=200 )

    return Response(serializer.errors, status=400)

@api_view(['DELETE','GET'])
def delete_student(request,id):
    stud=Student.objects.get(id=id)
    serializer = StudentSerializer(stud)
    stud.delete()
    return Response(serializer.data,status=200 )#status=status.HTTP_400_BAD_REQUEST
