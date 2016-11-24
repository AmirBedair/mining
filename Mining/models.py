from __future__ import unicode_literals

from django.db import models



class Contact(models.Model):
    name= models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject= models.CharField(max_length=500)
    message = models.CharField(max_length=20000)
    m_date = models.DateTimeField('date published')

