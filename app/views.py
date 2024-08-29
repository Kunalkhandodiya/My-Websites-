from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'templates/index.html')
def about(request):
    return render(request, 'templates/about.html')
def canteen(request):
    return render(request, 'templates/canteen.html')
def computerlabs(request):
    return render(request, 'templates/computer_labs.html')
def eligibilty(request):
    return render(request, 'templates/Eligibilty.html')
def Facultylogin(request):
    return render(request, 'templates/Faculity_Login.html')
def faculty(request):
    return render(request, 'templates/faculty.html')
def Fullyac(request):
    return render(request, 'templates/Fully_Ac.html')
def hostels(request):
    return render(request, 'templates/Hostels.html')
def Library(request):
    return render(request, 'templates/Library.html')
def Loginicon(request):
    return render(request, 'templates/Login_icon.html')
def Onlineadmission(request):
    return render(request, 'online_admissions.html')
def Privacy(request):
    return render(request, 'templates/privacy_policy.html')
def Signup(request):
    return render(request, 'templates/Sign_up.html')
def Studentlogin(request):
    return render(request, 'templates/Student_Login.html')

from app.forms import StudentRegistrationForm

def StudentRegistration(request):
    if request.method=="POST":
        form=StudentRegistrationForm(data=request.POST)

        if form.is_valid():
            form.save()
    else:
        form=StudentRegistrationForm()
    return render(request, "templates/online_admissions.html",{"form": form})
