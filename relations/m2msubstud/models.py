from django.db import models


class Subject(models.Model):
    code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} : {self.name}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    subjects = models.ManyToManyField(
        Subject,
        related_name="students"
    )

    def __str__(self):
        return self.name