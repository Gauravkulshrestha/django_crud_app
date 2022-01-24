from dataclasses import field
from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "fee"]

admin.site.register(Student, StudentAdmin)