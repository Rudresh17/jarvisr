from django import forms
from datetime import datetime
from django.forms import ModelForm
from django.db import models
from login.models import login



class todo(forms.ModelForm):
    class Meta:
        model=login
        fields={"name","email"}


   
        
        

