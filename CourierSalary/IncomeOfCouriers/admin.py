from django.contrib import admin

from .models import CourierProfile, Trip, CourierIncomeChange, CourierDailySalary, CourierWeeklySalary

# Register your models here.
admin.site.register(CourierProfile)
admin.site.register(Trip)
admin.site.register(CourierIncomeChange)
admin.site.register(CourierDailySalary)
admin.site.register(CourierWeeklySalary)
