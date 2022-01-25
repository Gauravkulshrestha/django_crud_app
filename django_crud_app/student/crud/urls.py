from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('deletestudent/<int:id>', views.deletestudent, name="deletestudent"),
    path('createstudent/', views.createstudent, name="createstudent"),
    path('updatestudent/<int:id>', views.updatestudent, name="updatestudent"),
]