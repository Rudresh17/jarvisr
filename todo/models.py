from django.db import models
from datetime import datetime
from django import forms
from django.forms import ModelForm



# Create your models here.

class addd(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title

    


    
   
