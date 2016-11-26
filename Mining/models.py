from __future__ import unicode_literals

from django.db import models



class Contact(models.Model):
    name= models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject= models.CharField(max_length=500)
    message = models.CharField(max_length=20000)
    m_date = models.DateTimeField('date published')

class Product(models.Model):
    name= models.CharField(max_length=200)
    descrition = models.CharField(max_length=1200)
    cacO3= models.CharField(max_length=20)
    caO = models.CharField(max_length=20)
    fe2O3 = models.CharField(max_length=20)
    mgO = models.CharField(max_length=20)
    al2O3 = models.CharField(max_length=20)
    SiO2 = models.CharField(max_length=20)
    loi = models.CharField(max_length=20)
    grainsize= models.CharField(max_length=1200)
    density = models.CharField(max_length=20)
    refractive = models.CharField(max_length=20)
    phvalue = models.CharField(max_length=20)
    bulkdensity = models.CharField(max_length=20)
    hardness = models.CharField(max_length=20)
    moisture = models.CharField(max_length=20)

