from django.shortcuts import render,redirect
from login.forms import todo
from django.http import HttpResponseRedirect
from home.views import index
from bs4 import BeautifulSoup
from newsapi import NewsApiClient
from urllib.request import urlopen


def indexx(request):
    name=""
    email=""
    form=todo()
    if request.method=="POST":
        form=todo(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']

            return render(request,"home/home.html",{"name":name,"email":email,"form":form})

    return render(request,"login/index.html",{"name":name,"email":email,"form":form})
    
   # url="https://www.moneycontrol.com/india/stockpricequote/auto-lcvs-hcvs/ashokleyland/AL"
   # page=urlopen(url)
   # soup=BeautifulSoup(page,"html.parser")
   # share=soup.find(id="Bse_Prc_tick")
   # newsapi = NewsApiClient(api_key='e79d7eb90e514647ac6aa24a9ceadd60')
   # top_headlines =newsapi.get_top_headlines(sources='the-times-of-india')
   # headlines=[]

   # for r in range(0,6):
   #     headlines.append(top_headlines["articles"][r]["title"])

    


            #return HttpResponseRedirect("http://localhost:8000/",{"name":name,"email":email})
            #return redirect(index,name=name,email=email)


   # return render(request,"login/index.html",{"form":todo})

    #return render(request,"home/home.html",{"price":share,"news":headlines,"name":name,"email":email})