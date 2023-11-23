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

def forgotpass(request):
    return render(request, 'vawc/forgot-pass.html')

def code(request):
    return render(request, 'vawc/send-code.html')

def newpass(request):
    return render(request, 'vawc/new-pass.html')

def doneSetPass(request):
    return render(request, 'vawc/done-setpass.html')

# Barangay side.
def barangay(request):
    return render(request, 'vawc/barangay/barangay-dashboard.html')

def barreport(request):
    return render(request, 'vawc/barangay/barangay-report.html')

def victimInfo(request):
    return render(request, 'vawc/barangay/barangay-victimInfo.html')

def perpetInfo(request):
    return render(request, 'vawc/barangay/barangay-perpetInfo.html')

def incidentInfo(request):
    return render(request, 'vawc/barangay/barangay-incidentInfo.html')

def servicesInfo(request):
    return render(request, 'vawc/barangay/barangay-servicesInfo.html')

def referred(request):
    return render(request, 'vawc/barangay/barangay-referred.html')

def myProfile(request):
    return render(request, 'vawc/barangay/barangay-myprofile.html')

def settings(request):
    return render(request, 'vawc/barangay/barangay-settings.html')

#  bpo.
def reportAddBpo(request):
    return render(request, 'vawc/barangay/barangay-report-add-bpo.html')

def bpo(request):
    return render(request, 'vawc/barangay/barangay-bpo.html')

def addBpo(request):
    return render(request, 'vawc/barangay/barangay-add-bpo.html')

# Police side.
def police(request):
    return render(request, 'vawc/police/police-dashboard.html')

# dswd side.
def dswd(request):
    return render(request, 'vawc/dswd/dswd-dashboard.html')
