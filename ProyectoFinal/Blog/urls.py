from django.contrib import admin
from django.urls import path, include

from Blog.views import (
    buscar_autor,
    buscar_articulo,
    buscar_seccion,
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
    path("buscar-seccion/", buscar_seccion, name="buscar-seccion"),
    path("buscar-articulo/", buscar_articulo, name="buscar-articulo"),
    path("buscar-autor/", buscar_autor, name="buscar-autor"),
]
