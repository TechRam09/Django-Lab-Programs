from django.contrib import admin
from django.urls import path
from app1.views import current_datetime

urlpatterns = [
    path('cdt/',current_datetime)
]