from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def report(request):
    context = {
        'student_name': 'Rishabh Kumar',
        'roll_number': 101,
        'class_name': '12th Grade',
        'attendance': 95,
        'is_passed': True,
        'total_marks': 425,
        'percentage': 85.0,
        
        # List of subjects with marks
        'subjects': [
            {'name': 'Mathematics', 'marks': 95, 'total': 100},
            {'name': 'Physics', 'marks': 88, 'total': 100},
            {'name': 'Chemistry', 'marks': 65, 'total': 100},
            {'name': 'English', 'marks': 78, 'total': 100},
            {'name': 'Computer Science', 'marks': 92, 'total': 100},
        ],
        
        # List of hobbies
        'hobbies': ['Reading', 'Coding', 'Cricket', 'Photography']
    }
    
    return render(request,'report.html',context)
