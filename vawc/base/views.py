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

#  behalf impact.
def behalfImpactVic(request):
    return render(request, 'vawc/barangay/barangay-behalfImpactedVic.html')

def behalfImpactVicStatus(request):
    return render(request, 'vawc/barangay/barangay-behalfImpactedVic-status.html')

def behalfImpactVicContact(request):
    return render(request, 'vawc/barangay/barangay-behalfImpactedVic-contact.html')

def behalfImpactVicVictim(request):
    return render(request, 'vawc/barangay/barangay-behalfImpactedVic-victim.html')

def behalfImpactVicPerpetrator(request):
    return render(request, 'vawc/barangay/barangay-behalfImpactedVic-perpetrator.html')

def behalfImpactVicIncident(request):
    return render(request, 'vawc/barangay/barangay-behalfImpactedVic-incident.html')

def behalfImpactVicIncident(request):
    return render(request, 'vawc/barangay/barangay-behalfImpactedVic-incident.html')

# end  file a report.

# services
def allServices(request):
    return render(request, 'vawc/barangay/barangay-all-services.html')

def servicesRescue(request):
    return render(request, 'vawc/barangay/barangay-rescue.html')

def servicesRescueStatus(request):
    return render(request, 'vawc/barangay/barangay-rescue-status.html')

def servicesRescueVictim(request):
    return render(request, 'vawc/barangay/barangay-rescue-victim.html')

def servicesRescuePerpetrator(request):
    return render(request, 'vawc/barangay/barangay-rescue-perpetrator.html')

def servicesRescueIncident(request):
    return render(request, 'vawc/barangay/barangay-rescue-incident.html')

def servicesRescueServices(request):
    return render(request, 'vawc/barangay/barangay-rescue-services.html')

def servicesRescueAddRef(request):
    return render(request, 'vawc/barangay/barangay-rescue-add-ref.html')

def servicesRescueRefView(request):
    return render(request, 'vawc/barangay/barangay-rescue-ref-view.html')



def servicesBpo(request):
    return render(request, 'vawc/barangay/barangay-bpo.html')

def servicesBpoStatus(request):
    return render(request, 'vawc/barangay/barangay-bpo-status.html')

def servicesBpoVictim(request):
    return render(request, 'vawc/barangay/barangay-bpo-victim.html')

def servicesBpoPerpetrator(request):
    return render(request, 'vawc/barangay/barangay-bpo-perpetrator.html')

def servicesBpoIncident(request):
    return render(request, 'vawc/barangay/barangay-bpo-incident.html')

def servicesBpoServices(request):
    return render(request, 'vawc/barangay/barangay-bpo-services.html')

def servicesBpoAddRef(request):
    return render(request, 'vawc/barangay/barangay-bpo-add-ref.html')

def servicesBpoRefView(request):
    return render(request, 'vawc/barangay/barangay-bpo-view-ref.html')

# end of services 

# records
def victim(request):
    return render(request, 'vawc/barangay/barangay-victim.html')

def victimStatus(request):
    return render(request, 'vawc/barangay/barangay-victim-status.html')

def victimVictim(request):
    return render(request, 'vawc/barangay/barangay-victim-victim.html')

def victimPerpetrator(request):
    return render(request, 'vawc/barangay/barangay-victim-perpetrator.html')

def victimIncident(request):
    return render(request, 'vawc/barangay/barangay-victim-incident.html')

def victimServices(request):
    return render(request, 'vawc/barangay/barangay-victim-services.html')

def victimAddRef(request):
    return render(request, 'vawc/barangay/barangay-victim-add-ref.html')

def victimRefView(request):
    return render(request, 'vawc/barangay/barangay-victim-ref-view.html')

def perpetrator(request):
    return render(request, 'vawc/barangay/barangay-perpetrator.html')

def perpetratorStatus(request):
    return render(request, 'vawc/barangay/barangay-perpetrator-status.html')

def perpetratorVictim(request):
    return render(request, 'vawc/barangay/barangay-perpetrator-victim.html')

def perpetratorPerpetrator(request):
    return render(request, 'vawc/barangay/barangay-perpetrator-perpetrator.html')

def perpetratorIncident(request):
    return render(request, 'vawc/barangay/barangay-perpetrator-incident.html')

def perpetratorServices(request):
    return render(request, 'vawc/barangay/barangay-perpetrator-services.html')

def perpetratorAddRef(request):
    return render(request, 'vawc/barangay/barangay-perpetrator-addRef.html')

def perpetratorRefView(request):
    return render(request, 'vawc/barangay/barangay-perpetrator-ref-view.html')
# end records

# cases
def openCases(request):
    return render(request, 'vawc/barangay/barangay-open-cases.html')

def openViewStatus(request):
    return render(request, 'vawc/barangay/barangay-open-view-status.html')

def openViewVictim(request):
    return render(request, 'vawc/barangay/barangay-open-victim-view.html')

def openViewPerpetrator(request):
    return render(request, 'vawc/barangay/barangay-open-perpetrator-view.html')

def openViewIncident(request):
    return render(request, 'vawc/barangay/barangay-open-incident-view.html')

def openViewServices(request):
    return render(request, 'vawc/barangay/barangay-open-services-view.html')

def openAddRef(request):
    return render(request, 'vawc/barangay/barangay-open-add-ref.html')

def openRefView(request):
    return render(request, 'vawc/barangay/barangay-open-ref-view.html')

def closeCases(request):
    return render(request, 'vawc/barangay/barangay-close-cases.html')

def closeCasesViewStatus(request):
    return render(request, 'vawc/barangay/barangay-close-view-status.html')

def closeVictimView(request):
    return render(request, 'vawc/barangay/barangay-close-victim-view.html')

def closePerpetratorView(request):
    return render(request, 'vawc/barangay/barangay-close-perpetrator-view.html')

def closeIncidentView(request):
    return render(request, 'vawc/barangay/barangay-close-incident-view.html')

def closeServicesView(request):
    return render(request, 'vawc/barangay/barangay-close-services-view.html')

def closeAddRef(request):
    return render(request, 'vawc/barangay/barangay-close-add-ref.html')

def closeRefView(request):
    return render(request, 'vawc/barangay/barangay-close-referral-view.html')
# end cases
# applicable for all



# end applicable for all

# report and feedback.
def monthlyReport(request):
    return render(request, 'vawc/barangay/barangay-monthlyReport.html')

def feedback(request):
    return render(request, 'vawc/barangay/barangay-feedback.html')

def feedbackForm(request):
    return render(request, 'vawc/barangay/barangay-feedback-form.html')

def feedbackFormView(request):
    return render(request, 'vawc/barangay/barangay-feedback-form-view.html')
# end of report and feedback.

# user settings.
def myProfile(request):
    return render(request, 'vawc/barangay/barangay-myprofile.html')


def settings(request):
    return render(request, 'vawc/barangay/barangay-settings.html')


