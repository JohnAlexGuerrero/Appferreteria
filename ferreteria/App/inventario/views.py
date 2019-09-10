from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def Hola(request):
    return HttpResponse('hi world')

def fecha_actual(request):
    ahora = datetime.datetime.now()
    html = "<html><body><h1>Fecha:</h1><h3>%s<h/3></body></html>"%ahora
    return HttpResponse(html)