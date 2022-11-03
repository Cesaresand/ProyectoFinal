from django.test import TestCase

from Blog.models import Autor

# Create your tests here.


class ViewTestCase(TestCase):
    def test_crear_autor(self):
        Autor.objects.create(
            nombre="Nombre1", apellido="Apellido1", profesion="Profesion1"
        )
        Autor.objects.create(
            nombre="Nombre2", apellido="Apellido2", profesion="Profesion2"
        )
        todos_los_autores = Autor.objects.all()

        assert len(todos_los_autores) == 2
        assert todos_los_autores[0].nombre == "Nombre1"
        assert todos_los_autores[0].apellido == "Apellido1"
        assert todos_los_autores[0].profesion == "Profesion1"
        assert todos_los_autores[1].nombre == "Nombre2"
        assert todos_los_autores[1].apellido == "Apellido2"
        assert todos_los_autores[1].profesion == "Profesion2"
