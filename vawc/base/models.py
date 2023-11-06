from django.db import models

# Create your models here.

class Barangay(models.Model):
    barangayName = models.CharField(max_length=200)
    barangayAddress = models.CharField(max_length=200, blank=True)
    fullname = models.CharField(max_length=200)
    #barangay = models.CharField(max_length=200)
    contactNum = models.CharField(max_length=20)
    email = models. CharField(max_length=100, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname
    
    