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
    path('signup/', views.signup, name="signup"),
    path('forgot-pass/', views.forgotpass, name="forgot password"),
    path('send-code/', views.code, name="send code"),
    path('new-pass/', views.newpass, name="new password"),
    path('done-setpass/', views.doneSetPass, name="Password Set Up Done"),
    path('barangay/dashboard', views.barangay, name="barangay"),
    path('barangay/report', views.barreport, name="barangay report"),
    path('barangay/victimInform', views.victimInfo, name="barangay victim info"),
    path('barangay/perpetInform', views.perpetInfo, name="barangay perpetrator info"),
    
    path('barangay/IncidentInform', views.incidentInfo, name="barangay incident info"),
    
    path('barangay/servicesInfo', views.servicesInfo, name="barangay services info"),
    
    path('barangay/report/add-bpo', views.reportAddBpo, name="barangay report add bpo"),
    
    path('barangay/referred', views.referred, name="barangay referred"),
    
    path('barangay/bpo', views.bpo, name="barangay bpo"),
    
    path('barangay/add-bpo', views.addBpo, name="barangay add bpo"),
    
    path('barangay/myprofile', views.myProfile, name="barangay my profile"),
    
    path('barangay/settings', views.settings, name="barangay settings"),
    
    
   
    
    
    
 
    
    path('police/dashboard', views.police, name="police"),
    path('dswd/dashboard', views.dswd, name="dswd"),
    
]