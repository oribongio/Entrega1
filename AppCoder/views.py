from django.shortcuts import render
from django.http import HttpResponse 
from .models import Curso 
from AppCoder.forms import cursoFormulario
# Create your views here.

def curso(request):
    curso=Curso(nombre="Curso de Python", comision=123456)
    curso.save
    texto =f"Curso Creado: nombre: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)

def cursoFormulario(request):
    
    if request.method =="POST":
        miFormulario= cursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info= miFormulario.cleaned_data
            nombre=info.get("nombre")
            comision=info.get("comision")
            curso=Curso(nombre=nombre, comision=comision)
            curso.save()
            return render (request, "AppCoder/inicio.html", { "mensaje" : "curso creado"})
        else:
            return render(request, "AppCoder/cursoFormulario.html", {"mensaje" : "error"})
    else: 
        miFormulario=cursoFormulario()
        return render (request, "AppCoder/cursoFormulario.html", {"formulario":miFormulario})

    # return render (request, "AppCoder/cursoFormulario.html")

def busquedaComision(request):
    return render(request, "AppCoder/busquedaComision.html")

def buscar(request):
    comi=request.GET("comision")
    # comision= request.GET.get("comision")
    # curso=Curso.objects.get(comision=comi)
    cursos=Curso.objects.filter(comision=comi)
    if len(cursos != 0):
        return render (request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos})
    else:
        return render(request, "AppCoder/resultadosBusqueda.html", {"mensaje" : "no hay cursos"})
