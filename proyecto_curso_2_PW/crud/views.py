from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#Importar Modelo
from .models import Dulce

# Create your views here.
def index(request):
    #Consultar el listado de registros de la tienda en la base de datos
    lista_dulces = Dulce.objects.all()
    template = loader.get_template("index.html")
    #Agregar los dulces al contexto del template
    context = {"dulces":lista_dulces}
    return HttpResponse(template.render(context,request))

def vista_detalle(request,id_dulce):
    #consultar los registros de los dulces de la tienda en la base de datos
    detalle_dulce = Dulce.objects.get(id = id_dulce)
    #obtener el template
    template = loader.get_template("detail.html")
    #Agregar los datos de los registros de la tienda al contexto del template
    context = {"dulce":detalle_dulce}
    return HttpResponse(template.render(context,request))