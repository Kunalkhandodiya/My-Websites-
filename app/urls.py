from django.contrib import admin
from app import views
from django.urls import path, reverse

urlpatterns = [
    
    path("",views.home, name="home"),
    path("about/",views.about, name="about"),
    path("canteen/",views.canteen, name="canteen"),
    path("computerlabs/", views.computerlabs, name="computerlabs"),
    path("eligibilty/", views.eligibilty, name="eligibilty"),
    path("Facultylogin/", views.Facultylogin, name="Facultylogin"),
    path("faculty/", views.faculty, name="faculty"),
    path("Fullyac/", views.Fullyac, name="Fullyac"),
    path("hostels/", views.hostels, name="hostels"),
    path("Library/", views.Library, name="Library"),
    path("Loginicon/", views.Loginicon, name="Loginicon"),
    path("Onlineadmission/", views.Onlineadmission, name="Onlineadmission"),
    path("Privacy/", views.Privacy, name="Privacy"),
    path("Signup/", views.Signup, name="Signup"),
    path("Studentlogin/", views.Studentlogin, name="Studentlogin"),
    path("form/",views.StudentRegistration, name="StudentRegistration"),




]
