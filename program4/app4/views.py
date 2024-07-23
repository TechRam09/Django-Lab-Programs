from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template

def layout(request):
    return render(request,'layout.html')

def home(request):
    return render(request,'home.html')

def aboutUs(request):
    return render(request,'aboutUs.html')

def contactUs(request):
    return render(request,'contactUs.html')