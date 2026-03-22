from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    bio=models.TextField()
    address=models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.student.name}"