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
    
    path('barangay/referred', views.referred, name="barangay referred"),
    
    path('barangay/victimInform', views.victimInfo, name="barangay victim info"),
    
    path('barangay/perpetInform', views.perpetInfo, name="barangay perpetrator info"),
    
    path('barangay/IncidentInform', views.incidentInfo, name="barangay incident info"),
    
    path('barangay/servicesInfo', views.servicesInfo, name="barangay services info"),
    
    path('barangay/add-crisis', views.servicesAddCrisis, name="barangay services add crisis"),
    
    path('barangay/add-bpo', views.servicesAddBPO, name="barangay services add bpo"),
    
    path('barangay/impacted-victim', views.impactVic, name="barangay report impact victim"),
    
    path('barangay/impacted-victim-status', views.impactVicStatus, name="barangay report impact victim status"),
    
    path('barangay/impacted-victim-victim', views.impactVicVictim, name="barangay report impact victim victim"),
    
    path('barangay/impacted-victim-perpetrator', views.impactVicPerpetrator, name="barangay report impact victim perpetrator"),
    
    path('barangay/impacted-victim-incident', views.impactVicIncident, name="barangay report impact victim incident"),
    
    path('barangay/impacted-victim-services', views.impactVicServices, name="barangay report impact victim services"),
    
    path('barangay/impacted-victim-add-ref', views.impactVicAddRef, name="barangay report impact victim add ref"),
    
    path('barangay/impacted-victim-view-ref', views.impactVicViewRef, name="barangay report impact victim view ref"),
    
    path('barangay/impacted-behalf-impacted-victim', views.behalfImpactVic, name="barangay report behalf impact victim"),
    
    path('barangay/impacted-behalf-impacted-victim-status', views.behalfImpactVicStatus, name="barangay report behalf impact victim status"),
    
    path('barangay/impacted-behalf-impacted-victim-contact', views.behalfImpactVicContact, name="barangay report behalf impact contact person"),
    
    path('barangay/impacted-behalf-impacted-victim-victim', views.behalfImpactVicVictim, name="barangay report behalf impact victim victim"),
    
    path('barangay/impacted-behalf-impacted-victim-perpetrator', views.behalfImpactVicPerpetrator, name="barangay report behalf impact victim perpetrator"),
    
    path('barangay/impacted-behalf-impacted-victim-incident', views.behalfImpactVicIncident, name="barangay report behalf impact victim incident"),
    
    path('barangay/impacted-behalf-impacted-victim-services', views.behalfImpactVicServices, name="barangay report behalf impact victim services"),
    
    path('barangay/impacted-behalf-impacted-victim-add-ref', views.behalfImpactVicAddRef, name="barangay report behalf impact victim add ref"),
    
    path('barangay/impacted-behalf-impacted-victim-view-ref', views.behalfImpactVicViewRef, name="barangay report behalf impact victim view ref"),
    
    path('barangay/all-services', views.allServices, name="barangay all services"),
    
    path('barangay/services-rescue', views.servicesRescue, name="barangay rescue"),
    
    path('barangay/services-rescue-status', views.servicesRescueStatus, name="barangay rescue status"),
    
    path('barangay/services-rescue-victim', views.servicesRescueVictim, name="barangay rescue victim"),
     
    path('barangay/services-rescue-perpetrator', views.servicesRescuePerpetrator, name="barangay rescue perpetrator"),
    
    path('barangay/services-rescue-incident', views.servicesRescueIncident, name="barangay rescue incident"),
    
    path('barangay/services-rescue-services', views.servicesRescueServices, name="barangay rescue services"),
    
    path('barangay/services-rescue-add-ref', views.servicesRescueAddRef, name="barangay rescue add ref"),
    
     path('barangay/services-rescue-ref-view', views.servicesRescueRefView, name="barangay rescue ref view"),
    
    path('barangay/bpo', views.servicesBpo, name="barangay bpo"),
    
    path('barangay/bpo-status', views.servicesBpoStatus, name="barangay bpo status"),
    
    path('barangay/bpo-victim', views.servicesBpoVictim, name="barangay bpo victim"),
    
    path('barangay/bpo-perpetrator', views.servicesBpoPerpetrator, name="barangay bpo perpetrator"),
    
    path('barangay/bpo-incident', views.servicesBpoIncident, name="barangay bpo incident"),
    
    path('barangay/bpo-services', views.servicesBpoServices, name="barangay bpo services"),
    
    path('barangay/bpo-add-ref', views.servicesBpoAddRef, name="barangay bpo add ref"),
    
     path('barangay/bpo-ref-vew', views.servicesBpoRefView, name="barangay bpo ref view"),
    
    path('barangay/victim', views.victim, name="barangay victim"),
    
    path('barangay/victim-status', views.victimStatus, name="barangay victim status"),
    
    path('barangay/victim-victim', views. victimVictim, name="barangay victim victim"),
    
    path('barangay/victim-perpetrator', views. victimPerpetrator, name="barangay victim perpetrator"),
    
    path('barangay/victim-incident', views. victimIncident, name="barangay victim incident"),
    
    path('barangay/victim-services', views. victimServices, name="barangay victim services"),

    path('barangay/victim-add-ref', views. victimAddRef, name="barangay victim add ref"),
    
    path('barangay/victim-ref', views.  victimRefView, name="barangay victim view ref"),
    
    path('barangay/perpetrator', views.perpetrator, name="barangay perpetrator"),
    
    path('barangay/perpetrator-status', views.perpetratorStatus, name="barangay perpetrator status"),
    
    path('barangay/perpetrator-victim', views.perpetratorVictim, name="barangay perpetrator victim"),
    
    path('barangay/perpetrator-perpetrator', views.perpetratorPerpetrator, name="barangay perpetrator perpetrator"),
    
    path('barangay/perpetrator-incident', views.perpetratorIncident, name="barangay perpetrator incident"),
    
    path('barangay/perpetrator-services', views.perpetratorServices, name="barangay perpetrator services"),
    
    path('barangay/perpetrator-addRef', views.perpetratorAddRef, name="barangay perpetrator add ref"),
    
    path('barangay/perpetrator-ref-view', views.perpetratorRefView, name="barangay perpetrator ref view"),
    
    path('barangay/open-cases', views.openCases, name="barangay open cases"),
    
    path('barangay/open-status-view', views.openViewStatus, name="barangay open view status"),
    
    path('barangay/open-victim-view', views.openViewVictim, name="barangay open victim view"),
    
    path('barangay/open-perpetrator-view', views.openViewPerpetrator, name="barangay open perpetrator view"),
    
    path('barangay/open-incident-view', views.openViewIncident, name="barangay open incident view"),
    
    path('barangay/open-services-view', views.openViewServices, name="barangay open services view"),
    
    path('barangay/open-addReferral', views.openAddRef, name="barangay open add ref"),
    
    path('barangay/open-referral-view', views.openRefView, name="barangay open ref view"),

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
    
     
    
]

