from django.conf.urls import url
from todo import views

urlpatterns = [
    url("^$",views.indexx,name="index"),
    url("/show",views.show,name="index"),
    
   
    
]