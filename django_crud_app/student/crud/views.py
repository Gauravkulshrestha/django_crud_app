import re
from tkinter import N
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Student
# Create your views here.

def home(request):
    students = Student.objects.all()
    context = {"students": students}

    return render(request, "home.html", context)

def deletestudent(id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("home")

def createstudent(request):
    if request.method == "POST":
        name = request.POST.get("name")
        fee = request.POST.get("fee")

        student = Student(name=name,fee=fee)
        student.save()
    return redirect("home") 