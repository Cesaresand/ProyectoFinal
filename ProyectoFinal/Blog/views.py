from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from Blog.models import Articulo, Autor, Seccion
from Blog.forms import ArticuloForm, AutorForm, SeccionForm


def buscar(request):

    if request.method == "GET":
        return render(request, "Blog/formulario-de-busqueda.html")

    if request.method == "POST":

        titulo_para_buscar = request.POST["titulo"]
        resultados_de_busqueda = Articulo.objects.filter(
            titulo=titulo_para_buscar
        )  ## esto es para buscar en la base de datos
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "Blog/resultado-de-la-busqueda.html", context=contexto)


####################################################################################
def mostrar_inicio(request):
    return render(request, "Blog/inicio.html")


#####################################################################################
def procesar_formulario_autor(request):

    if request.method == "GET":

        mi_formulario = AutorForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "Blog/formulario-autor.html", context=contexto)

    if request.method == "POST":

        mi_formulario = AutorForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Autor(
                nombre=datos_ingresados_por_usuario["nombre"],
                apellido=datos_ingresados_por_usuario["apellido"],
                profesion=datos_ingresados_por_usuario["profesion"],
            )
            nuevo_modelo.save()

            return render(request, "Blog/agradecimiento.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "Blog/formulario-autor.html", context=contexto)


#######################################################################################
def procesar_formulario_articulo(request):

    ##breakpoint() para hacer un debugger
    if request.method == "GET":

        mi_formulario = ArticuloForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "Blog/formulario-articulo.html", context=contexto)

    if request.method == "POST":

        mi_formulario = ArticuloForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Articulo(
                titulo=datos_ingresados_por_usuario["titulo"],
                texto=datos_ingresados_por_usuario["texto"],
                fecha=datos_ingresados_por_usuario["fecha"],
            )
            nuevo_modelo.save()

            return render(request, "Blog/agradecimiento.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "Blog/formulario-articulo.html", context=contexto)


########################################################################################
def procesar_formulario_seccion(request):

    if request.method == "GET":
        mi_formulario = SeccionForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "Blog/formulario-seccion.html", context=contexto)

    if request.method == "POST":

        mi_formulario = SeccionForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Seccion(
                nombre=datos_ingresados_por_usuario["nombre"],
            )
            nuevo_modelo.save()

            return render(request, "Blog/agradecimiento.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "Blog/formulario-seccion.html", context=contexto)
