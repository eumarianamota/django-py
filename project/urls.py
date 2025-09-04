
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


# HTTP Request
def home(request):
    return HttpResponse("HOME")


def sobre(request):
    return HttpResponse("SOBRE")


def contato(request):
    return HttpResponse("CONTATO")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),

]
