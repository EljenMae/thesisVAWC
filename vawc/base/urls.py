from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('report/', views.report, name="report"),
    
    path('impact-victim-survivor/', views.impactVictim, name="impact victim"),
    
    path('impact-perpetrator/', views.impactPerpetrator, name="impact perpetrator"),
    
    path('impact-incident/', views.impactIncident, name="impact incident"),
    
    path('impact-service/', views.impactService, name="impact service"),
    
    path('impact-crisis/', views.impactCrisis, name="impact crisis"),
    
    path('impact-issuance/', views.impactIssuance, name="impact issuance"),
    
    path('behalf-contact-Person/', views.behalfContactPerson, name="behalf contact person"),
    
    path('behalf-victim/', views.behalfVictim, name="behalf victim"),
    
    path('behalf-perpetrator/', views.behalfPerpetrator, name="behalf perpetrator"),
    
    path('behalf-incident/', views.behalfIncident, name="behalf incident"),
    
    path('behalf-service/', views.behalfService, name="behalf service"),
    
    path('behalf-crisis/', views.behalfCrisis, name="behalf crisis"),
    
    path('behalf-issuance/', views.behalfIssuance, name="behalf issuance"),
    
    path('login/', views.login, name="login"),

    path('barangay/dashboard', views.barangay, name="barangay"),
    
    path('barangay/report', views.barreport, name="barangay report"),
    
    path('barangay/victimInform', views.victimInfo, name="barangay victim info"),
    path('barangay/perpetInform', views.perpetInfo, name="barangay perpetrator info"),
    
    path('barangay/IncidentInform', views.incidentInfo, name="barangay incident info"),
    
    path('barangay/servicesInfo', views.servicesInfo, name="barangay services info"),
    
    path('barangay/add-crisis', views.servicesAddCrisis, name="barangay services add crisis"),
    
    path('barangay/add-bpo', views.servicesAddBPO, name="barangay services add bpo"),
    
    path('barangay/impacted-victim', views.impactVic, name="barangay report impact victim"),
    
    path('barangay/impacted-behalf-impacted-victim', views.behalfImpactVic, name="barangay report behalf impact victim"),
    
    path('barangay/all-services', views.allServices, name="barangay all services"),
    
    path('barangay/services-rescue', views.servicesRescue, name="barangay rescue"),
    
    path('barangay/bpo', views.servicesBpo, name="barangay bpo"),
    
    path('barangay/referred', views.referred, name="barangay referred"),
    
   path('barangay/victim', views.victim, name="barangay victim"),
   
    path('barangay/perpetrator', views.perpetrator, name="barangay perpetrator"),
    
    path('barangay/open-cases', views.openCases, name="barangay open cases"),
    
    path('barangay/close-cases', views.closeCases, name="barangay close cases"),
    
    path('barangay/close-cases-view', views.closeCasesViewStatus, name="barangay close cases view status"),
       
    path('barangay/close-victim-view', views.closeVictimView, name="barangay close victim view"),
    
    path('barangay/close-perpetrator-view', views.closePerpetratorView, name="barangay close perpetrator view"),
    
    path('barangay/close-incident-view', views.closeIncidentView, name="barangay close incident view"),
    
    path('barangay/close-services-view', views.closeServicesView, name="barangay close services view"),
    
    path('barangay/close-add-ref', views.closeAddRef, name="barangay close add ref"),

    path('barangay/close-ref-view', views.closeRefView, name="barangay close ref view"),
    
    path('barangay/monthly-report', views.monthlyReport, name="barangay monthly report"),
    
    path('barangay/monthly-feedback', views.feedback, name="barangay feedback"),
    
    path('barangay/monthly-feedback-form', views.feedbackForm, name="barangay feedback form"),
    
    path('barangay/monthly-feedback-form-view', views.feedbackFormView, name="barangay feedback form view"),




    path('barangay/myprofile', views.myProfile, name="barangay my profile"),
    
    path('barangay/settings', views.settings, name="barangay settings"),
    
    
   
    
    
    

]