from django.db import models

# Create your models here.


  
class Agency(models.Model):
    agencyName = models.CharField(max_length=200)
    agencyAddress = models.CharField(max_length=200, blank=True)
    contactPerson = models.CharField(max_length=200)
    email = models. CharField(max_length=100, blank=True)
    contactNum = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname
    
class Barangay(models.Model):
    #user = 
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
