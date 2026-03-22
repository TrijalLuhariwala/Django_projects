from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.
def orm_prep(request):
    
    students = Student.objects.all()
    students_list = []
    
    # [o1,o2,o3]
    for s in students:
        students_list.append({
            'name': s.name,
            'age': s.age,
            'email': s.email,
        })
        
        # for JsonResponse --
        return JsonResponse(students_list, safe=False)
        
        # for HttpResponse --
        students_values = Student.objects.values()
        print(students_values)
        
        # get student by id --
        var_get_student_by_id = Student.objects.get(id = 4)
        # print(var_get_student_by_id)
        print(var_get_student_by_id.name)
        print(var_get_student_by_id.age)
        print(var_get_student_by_id.email)
        
        # get student by name --
        var_get_student_by_age = Student.objects.get(age = 22)
        # print(var_get_student_by_age)
        print(var_get_student_by_age.name)
        print(var_get_student_by_age.age)
        print(var_get_student_by_age.email)
        
        # get student by multiple fields --
        var_get_student_by_age = Student.objects.get(age = 22, name = 'Ravi', email = 'ravi01@gmail.com')
        var_get_student_by_age = Student.objects.filter(age = 22, name = 'Ravi')
        print(var_get_student_by_age.query)
        # output -- 
        # SELECT 
        # "myapp_student"."id", 
        # "myapp_student"."name", 
        # "myapp_student"."age", 
        # "myapp_student"."email" 
        # FROM "myapp_student" WHERE (
        # "myapp_student"."age" = 22 AND 
        # "myapp_student"."name" = Ravi)
        
        # get student by age greater than --
        greater_than = Student.objects.filter(age__gt = 19)
        print(greater_than)
        print(greater_than.query)
        # Output --(on terminal)
        # SELECT 
        # "myapp_student"."id", 
        # "myapp_student"."name", 
        # "myapp_student"."age", 
        # "myapp_student"."email" FROM 
        # "myapp_student" WHERE 
        # "myapp_student"."age" > 19
        
        # get students whose name contains 'av' --
        av_names = Student.objects.filter(name__icontains = 'av')
        print(av_names)
        print(av_names.query)
        # Output --
        # SELECT 
        # "myapp_student"."id", 
        # "myapp_student"."name", 
        # "myapp_student"."age", 
        # "myapp_student"."email" FROM 
        # "myapp_student" WHERE 
        # "myapp_student"."name" 
        # LIKE %av% ESCAPE '\'
        
        # Create a new student --
        new_student = Student.objects.create(name = 'Rakesh', age = 19, email = 'rakesh01@gmail.com')
        print(new_student)
        # output -- <Student: Rakesh>
        
        
        # Fetch students whose age is 21 OR name is 'Abhinav'
        from django.db.models import Q
        object_age_or_name = Student.objects.filter(Q(age = 21) | Q(name = 'Abhinav'))
        print(object_age_or_name)
        # Output --
        # [<Student: Abhinav>, <Student: Rahul>]>
        
        # check if student with name 'xyz' exists, if not create it --
        student_data, created = Student.objects.get_or_create(name = 'xyz', age = 12, email = 'xyz@gmail.com')
        print(student_data, created)
        # Output --
        # <Student: xyz> True, true means created, false means already exists
        
        # check if student with email exists, if yes update it, if not create it --
        student_data, created = Student.objects.update_or_create(email = 'xyzz@gmail.com', defaults = {'name': 'xyzz', 'age': 13})
        print(student_data, created)
        # Output --
        # <Student: xyzz> True, true means created, false means updated
        
        # check if student with email exists, if yes update it, if not create it --
        student_data, created = Student.objects.update_or_create(email = 'guptaa.amit@gmail.com', defaults = {'name': 'Gupta Amit', 'age': 44})
        print(student_data, created)
        # Output --
        # <Student: Gupta Amit> True    
        
        # delete students data with id(primary key)
        student_data = Student.objects.get(id = 3)
        deleted = student_data.delete()
        print(deleted)
        
        # delete students data which contains 'Ra' in their names by using filter 
        student_data = Student.objects.filter(name__icontains = 'Ra')
        Number_of_deleted_object = student_data.delete()
        print(Number_of_deleted_object)

startswith = Case-Sensitive starts-with.
Example = Students.objects.filter(name__startswith = 'r')

istartswith = Case-inSensitive starts-with.     
Example = Students.objects.filter(name__istartswith = 'r')

endswith = Case-Sensitive ends-with.
Example = Students.objects.filter(name__endswith = 'z')

iendswith = Case-inSensitive ends-with.
Example = Students.objects.filter(name__iendswith = 'z')


        return HttpResponse('All students')

# Check query here--
# C:\Users\rajat\OneDrive\Desktop\PEP\day15SaturdayDjango\myproject6\myapp\migrations\0001_initial.py