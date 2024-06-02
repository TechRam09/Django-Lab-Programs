from django.shortcuts import render
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<h1>It is now %s</h1>' % now
    return HttpResponse(html)

