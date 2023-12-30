from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request, 'vawc/home.html')

#  report.
def report(request):
    return render(request, 'vawc/report.html')

def impactVictim(request):
    return render(request, 'vawc/impacted-victim.html')

def impactPerpetrator(request):
    return render(request, 'vawc/impacted-perpetrator.html')

def impactIncident(request):
    return render(request, 'vawc/impacted-incident.html')

def impactService(request):
    return render(request, 'vawc/impacted-service.html')

def impactCrisis(request):
    return render(request, 'vawc/impacted-crisis.html')

def impactIssuance(request):
    return render(request, 'vawc/impacted-issuance.html')

def behalfContactPerson(request):
    return render(request, 'vawc/behalf-contactPerson.html')

def behalfVictim(request):
    return render(request, 'vawc/behalf-victim.html')

def behalfPerpetrator(request):
    return render(request, 'vawc/behalf-perpetrator.html')

def behalfIncident(request):
    return render(request, 'vawc/behalf-incident.html')

def behalfService(request):
    return render(request, 'vawc/behalf-service.html')

def behalfCrisis(request):
    return render(request, 'vawc/behalf-crisis.html')

def behalfIssuance(request):
    return render(request, 'vawc/behalf-issuance.html')

#  end of report.

#  log-in.
def login(request):
    return render(request, 'vawc/login.html')

# Barangay side.
def barangay(request):
    return render(request, 'vawc/barangay/barangay-dashboard.html')

# report side.
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

def servicesAddCrisis(request):
    return render(request, 'vawc/barangay/barangay-addCrisis.html')

def servicesAddBPO(request):
    return render(request, 'vawc/barangay/barangay-addBPO.html')

def referred(request):
    return render(request, 'vawc/barangay/barangay-referred.html')
# End of report.

#  file a report.
def impactVic(request):
    return render(request, 'vawc/barangay/barangay-impactedVic.html')

def behalfImpactVic(request):
    return render(request, 'vawc/barangay/barangay-behalfImpactedVic.html')

# end  file a report.

# services
def allServices(request):
    return render(request, 'vawc/barangay/barangay-all-services.html')

def servicesRescue(request):
    return render(request, 'vawc/barangay/barangay-rescue.html')

def servicesBpo(request):
    return render(request, 'vawc/barangay/barangay-bpo.html')

# end of services 

# records
def victim(request):
    return render(request, 'vawc/barangay/barangay-victim.html')

def perpetrator(request):
    return render(request, 'vawc/barangay/barangay-perpetrator.html')
# end records

# cases
def openCases(request):
    return render(request, 'vawc/barangay/barangay-open-cases.html')

def closeCases(request):
    return render(request, 'vawc/barangay/barangay-close-cases.html')
# end cases

# report and feedback.
def monthlyReport(request):
    return render(request, 'vawc/barangay/barangay-monthlyReport.html')
# end of report and feedback.

# user settings.
def myProfile(request):
    return render(request, 'vawc/barangay/barangay-myprofile.html')


def settings(request):
    return render(request, 'vawc/barangay/barangay-settings.html')


