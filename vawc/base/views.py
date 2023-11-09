from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request, 'vawc/home.html')

def report(request):
    return render(request, 'vawc/report.html')

def login(request):
    return render(request, 'vawc/login.html')

def signup(request):
    return render(request, 'vawc/signup.html')

def barangay(request):
    return render(request, 'vawc/barangay-dashboard.html')

def police(request):
    return render(request, 'vawc/police-dashboard.html')

def dswd(request):
    return render(request, 'vawc/dswd-dashboard.html')
