from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('report/', views.report, name="report"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('barangay/dashboard', views.barangay, name="barangay"),
    path('police/dashboard', views.police, name="police"),
    path('dswd/dashboard', views.dswd, name="dswd"),
    
]