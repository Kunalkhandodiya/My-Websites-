from django.db import models

COURSE_CHOICES = [
    ("BCA", "BCA"),
    ("BBA", "BBA"),
    ("MCA", "MCA"),
    ("B.Tech", "B.Tech"),
    ("MBA", "MBA"),
    ("M.Tech", "M.Tech"),
]

GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
]

class StudentRegistration(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=50)
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    course = models.CharField(choices=COURSE_CHOICES, max_length=10)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    phone = models.IntegerField()
    email=models.EmailField()
    current_address = models.CharField(max_length=500)


class Studentfees(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=50)
    father_name=models.CharField(max_length=100)
    course = models.CharField(choices=COURSE_CHOICES, max_length=10)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    phone = models.IntegerField()
    Current_fees=models.IntegerField()

class FacultyRegistration(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=50)
    father_name=models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    Education_Field = models.CharField(choices=COURSE_CHOICES, max_length=10)
    Higher_qualification=models.CharField(choices=COURSE_CHOICES, max_length=10)
    phone = models.IntegerField()
    Experience=models.IntegerField(default=0)
    Current_Salary=models.IntegerField(default=0)

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
