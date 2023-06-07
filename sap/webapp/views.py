from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def bienvenida (request):
    pagina = loader.get_template('saludo html')
    return HttpResponse(pagina.render())


def hola(request, nombre):
    apellido = request.GET['apellido']
    nivel = request.GET['nivel']
    curso = request.GET['curso']
    pagina = loader.get_template('saludo.html')
    nombreCompleto =  nombre +" " + apellido
    datos = {'nombre': nombreCompleto , 'curso':curso, 'nivel':nivel}
    return HttpResponse(pagina.render(datos, request))

def edad (request, edad):
    pagina = loader.get_template('edad.html')
    mensaje = {'edad': edad}
    return HttpResponse(pagina.render(mensaje, request))