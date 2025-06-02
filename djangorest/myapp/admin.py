from django.contrib import admin
from .models import *

# Register your models here.

class StudentList(admin.ModelAdmin):
    list_display=["name","age","email"]
    search_fields=["name","email"]



admin.site.register(Student,StudentList)

class DepartmentList(admin.ModelAdmin):
    list_display=["name"]

admin.site.register(Department,DepartmentList)