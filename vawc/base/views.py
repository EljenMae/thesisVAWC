from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def report(request):
    return render(request, 'report.html')
