from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'vawc/home.html')

def report(request):
    return render(request, 'vawc/report.html')

def dswd(request):
    return render(request, 'dswd-dashboard.html')

