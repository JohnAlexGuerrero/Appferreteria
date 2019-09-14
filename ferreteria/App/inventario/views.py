from django.shortcuts import render
from django.http import HttpResponse
import datetime
from App.inventario.models import Producto

# Create your views here.
def formulario_buscar(request):
    return render(request,'formulario_buscar.html')

def buscar(request):
    error = False

    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            error = True
        else:
            producto = Producto.objects.filter(descripcion__icontains = q)
            return render(request,'resultados.html',{'producto':producto,'query':q})
    
    return render(request,'formulario_buscar.html',{'error':error})