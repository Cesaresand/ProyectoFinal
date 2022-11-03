from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from Blog.models import Articulo, Autor, Seccion, Avatar, Pagina
from Blog.forms import ArticuloForm, AutorForm, SeccionForm, UserEditionForm, AvatarForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def buscar_articulo(request):
    if request.method == "GET":
        return render(request, "Blog/formulario-de-busqueda-articulo.html")

    if request.method == "POST":
        titulo_para_buscar = request.POST["titulo"]
        resultados_de_busqueda = Articulo.objects.filter(
            titulo=titulo_para_buscar
        )  ## esto es para buscar en la base de datos
        contexto = {"resultados": resultados_de_busqueda}
        return render(
            request, "Blog/resultado-de-la-busqueda-articulo.html", context=contexto
        )


#################################################################################


@login_required
def buscar_seccion(request):
    if request.method == "GET":
        return render(request, "Blog/formulario-de-busqueda-seccion.html")

    if request.method == "POST":
        seccion_para_buscar = request.POST["seccion"]
        resultados_de_busqueda = Seccion.objects.filter(
            seccion=seccion_para_buscar
        )  ## esto es para buscar en la base de datos
        contexto = {"resultados": resultados_de_busqueda}
        return render(
            request, "Blog/resultado-de-busqueda-seccion.html", context=contexto
        )


##########################################################################################


@login_required
def buscar_autor(request):
    if request.method == "GET":
        return render(request, "Blog/formulario-de-busqueda-autor.html")

    if request.method == "POST":

        nombre_para_buscar = request.POST["nombre"]
        resultados_de_busqueda = Autor.objects.filter(nombre=nombre_para_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(
            request, "Blog/resultado-de-busqueda-autor.html", context=contexto
        )


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
                email=datos_ingresados_por_usuario["email"],
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
                seccion=datos_ingresados_por_usuario["seccion"],
                texto=datos_ingresados_por_usuario["texto"],
                autor=datos_ingresados_por_usuario["autor"],
            )
            nuevo_modelo.save()

            return render(request, "Blog/agradecimiento.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "Blog/formulario-seccion.html", context=contexto)


#######################################################################################
# def mostrar_inicio(request):
#     return render(request, "Blog/inicio.html")


@login_required
def mostrar_inicio(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.imagen.url}
    else:
        contexto = {}

    return render(request, "Blog/inicio.html", contexto)


########################################################################################


def mostrar_acerca_de_mi(request):
    return render(request, "Blog/acerca-de-mi.html")


#########################################################################################
#########################################################################################


class AutorList(LoginRequiredMixin, ListView):
    model = Autor
    template_name = "Blog/autor_list.html"


class PaginasList(LoginRequiredMixin, ListView):
    model = Pagina
    template_name = "Blog/paginas_list.html"


class AutorDetalle(LoginRequiredMixin, DetailView):
    model = Autor
    template_name = "Blog/autor_detalle.html"


class PaginaDetalle(LoginRequiredMixin, DetailView):
    model = Pagina
    template_name = "Blog/pagina_detalle.html"


from django.urls import reverse


class AutorCreacion(LoginRequiredMixin, CreateView):
    model = Autor
    fields = ["nombre", "apellido", "profesion", "email"]
    success_url = "/Blog/autor/list"


class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    success_url = "/Blog/autor/list"
    fields = ["nombre", "apellido", "profesion", "email"]


class AutorDelete(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = "/Blog/autor/list"


class MyLogin(LoginView):
    template_name = "Blog/login.html"


class MyLogout(LoginRequiredMixin, LogoutView):
    template_name = "Blog/logout.html"


class PaginaCreacion(CreateView):
    model = Pagina
    fields = ["autor", "titulo", "texto", "fecha"]
    success_url = "/Blog/paginas/list"


class PaginaUpdateView(LoginRequiredMixin, UpdateView):
    model = Pagina
    success_url = "/Blog/paginas/list"
    fields = ["autor", "titulo", "subtitulo", "texto", "fecha"]


class PaginaDelete(LoginRequiredMixin, DeleteView):
    model = Pagina
    success_url = "/Blog/paginas/list"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "Blog/inicio.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserCreationForm()

    return render(request, "Blog/registro.html", {"form": form})


@login_required
def editar_perfil(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()

    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "blog/inicio.html", {"avatar": avatar.imagen.url})

    contexto = {"user": user, "form": form, "avatar": avatar.imagen.url}
    return render(request, "Blog/editarPerfil.html", contexto)


@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "Blog/inicio.html")

    contexto = {"form": form}
    return render(request, "Blog/avatar_form.html", contexto)


@login_required
def about_me(request):
    return render(request, "blog/acerca-de-mi.html")
