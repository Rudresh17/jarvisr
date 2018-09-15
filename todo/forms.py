from django import forms
from datetime import datetime
from django.forms import ModelForm
from .models import addd
from django.db import models



class todo(forms.ModelForm):
    class Meta:
        model=addd
        fields={"title","date"}


   
        
        

