from django.shortcuts import redirect, render
from .models import Student

def home(request):
    students = Student.objects.all()
    context = {"students": students}

    return render(request, "home.html", context)

def deletestudent(request, id):
    if request.method == "POST":
        student = Student.objects.get(id=id)
        student.delete()
    return redirect("home")

def createstudent(request):
    if request.method == "POST":
        name = request.POST.get("name")
        fee = request.POST.get("fee")
        Student.objects.create(name=name,fee=fee)
    return redirect("home")

def updatestudent(request,id):
    if request.method == "POST":
        student = Student.objects.get(id=id)        
        name = request.POST.get("name")
        fee = request.POST.get("fee")
        student.name = name
        student.fee = fee
        student.save()
    return redirect("home")