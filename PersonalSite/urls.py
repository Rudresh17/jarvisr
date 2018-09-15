
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include("login.urls")),
    path('home/', include("home.urls")),
    path("",include("login.urls")),
    path("routine",include("routine.urls")),
    path("todo",include("todo.urls")),
]
