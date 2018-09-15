from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from newsapi import NewsApiClient
from login.forms import todo

# Create your views here.

def index(request):

    if request.method=="POST":
        form=todo(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            url="https://www.moneycontrol.com/india/stockpricequote/auto-lcvs-hcvs/ashokleyland/AL"
            page=urlopen(url)
            soup=BeautifulSoup(page,"html.parser")
            share=soup.find(id="Bse_Prc_tick")
            newsapi = NewsApiClient(api_key='e79d7eb90e514647ac6aa24a9ceadd60')
            top_headlines =newsapi.get_top_headlines(sources='the-times-of-india')
            headlines=[]

        for r in range(0,6):
            headlines.append(top_headlines["articles"][r]["title"])

            return render(request,"home/home.html",{"name":name,"email":email,"price":share,"news":headlines})

   


    return render(request,"home/home.html",{"price":share,"news":headlines})


