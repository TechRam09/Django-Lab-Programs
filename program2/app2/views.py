from django.shortcuts import render
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<h1>It is now %s</h1>' % now
    return HttpResponse(html)

def four_hours_ahead(request):
    time = datetime.datetime.now() + datetime.timedelta(hours=4)
    html = '<h1> four hour ahead it is %s</h1>' % time
    return HttpResponse(html)

def four_hours_before(request):
    time = datetime.datetime.now() + datetime.timedelta(hours=-4)
    html = '<h1> four hour before it is %s</h1>' % time
    return HttpResponse(html)