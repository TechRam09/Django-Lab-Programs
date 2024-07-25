from django.shortcuts import render
from django.http import HttpResponse
from app5.models import Course,Student

def course_search(request):
    if request.method == 'POST':
        cid = request.POST.get('cname')
        s = Student.objects.all()
        student_list = list()
        for student in s:
            if student.enrolment.filter(id=cid):
                student_list.append(student)
        
        if len(student_list) == 0:
            return HttpResponse('<h1>No Students Enrolled</h1>')
        
        return render(request,'selected_students.html',{"student_list":student_list})
    
    else:
        courses = Course.objects.all()
        return render(request,'course_search.html',{"courses":courses})

# Create your views here.
