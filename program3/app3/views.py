from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template

def showlist(request):
 fruits=["Mango","Apple","Bananan","Jackfruits"]
 student_names=["Ajay","Balaji","Sony","Mohan"]
 return render(request,'showlist.html',{"fruits":fruits,"student_names":student_names})
