from django.contrib import admin
from django.db import models
from app.models import StudentRegistration,Studentfees
# Register your models here.


# for Manipulation admin panel
admin.empty_value_display = '**Empty**'
admin.site.site_header="Student Registration"
admin.site.site_title="student"
admin.site.site_url='http://127.0.0.1:8000/'
admin.site.index_title = 'Student Registration Table'
admin.site.


# StudenentRegistration
admin.site.register(StudentRegistration)


# Studentadmin 
class Studentadmin(admin.ModelAdmin):
    list_display=["first_name","last_name","course","Current_fees"]
    list_display_links=["first_name"]
    list_editable=["course"]
    list_per_page=5
    search_fields=["^first_name","^last_name"]
    list_filter=["course"]

admin.site.register(Studentfees,Studentadmin)    



