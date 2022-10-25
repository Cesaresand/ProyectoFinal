from django.contrib import admin
from django.urls import path, include

from Blog.views import (
    buscar,
    mostrar_inicio,
    procesar_formulario_autor,
    procesar_formulario_articulo,
    procesar_formulario_seccion,
)


urlpatterns = [
    path("inicio/", mostrar_inicio, name="inicio"),
    path("formulario-autor/", procesar_formulario_autor, name="registrar-autor"),
    path(
        "formulario-articulo/", procesar_formulario_articulo, name="registrar-articulo"
    ),
    path("formulario-seccion/", procesar_formulario_seccion, name="registrar-seccion"),
    path("buscar-articulo/", buscar, name="buscar-articulo"),
]
