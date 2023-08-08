from django.shortcuts import render, HttpResponse
import requests

# Create your views here.

def hola(request):
    productos = requests.get("http://codealberti1997.pythonanywhere.com/api/productos/")
    print(productos.json())
    lista = [i.get("nombre") for i in productos.json()]
    return HttpResponse(lista)

