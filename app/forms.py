from django import forms
from .models import StudentRegistration,Studentfees

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = "__all__"

class Studentfeesform(forms.ModelForm):
    class Meta:
        model=Studentfees
        fields="__all__"