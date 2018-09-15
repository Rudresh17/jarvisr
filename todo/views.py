from django.shortcuts import render
from django.http import HttpResponse
from .forms import todo
from .models import addd
from django.db import models
from django.db import connection


def indexx(request):
    form=todo(request.POST)
    if request.method=="POST":

        form=todo(request.POST)
        if form.is_valid():
            date=form.cleaned_data['date']
            title=form.cleaned_data['title']
            #addd.objects.raw('insert into todo_addd (title,date) values("done","1111")')
            form.save()
            
            
            
            
            return render(request,"todo/index.html",{"form":form}) 
    
    return render(request,"todo/index.html",{"form":form}) 

    
def show(request):  
       
       info=addd.objects.raw('select * from todo_addd')
       return render(request,"todo/index.html",{"form":info})

        
            
            
        
        
        
        

