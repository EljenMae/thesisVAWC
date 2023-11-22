from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('report/', views.report, name="report"),
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
    path('barangay/referred', views.referred, name="barangay referred"),
    
    
    path('barangay/myprofile', views.myProfile, name="barangay my profile"),
    
    path('barangay/settings', views.settings, name="barangay settings"),
    
    path('barangay/bpo', views.bpo, name="barangay bpo"),
    
    path('police/dashboard', views.police, name="police"),
    path('dswd/dashboard', views.dswd, name="dswd"),
    
]