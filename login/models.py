from django.db import models
from datetime import datetime
from django import forms
from django.forms import ModelForm


class login(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    