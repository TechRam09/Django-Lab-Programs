
from django.contrib import admin
from django.urls import path
from app2.views import current_datetime,four_hours_ahead,four_hours_before

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cdt/',current_datetime),
    path('fhrsa/',four_hours_ahead),
    path('fhrsb/',four_hours_before),
]
