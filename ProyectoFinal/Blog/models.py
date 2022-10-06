from django.db import models

# Create your models here.


class Autor(models.Model):
    class Meta:
        verbose_name_plural = "Autores" #ESTO sirve para corregir el nombre de Autor TIP!

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Articulo(models.Model):

    titulo = models.CharField(max_length=30)
    texto = models.CharField(max_length=1500)
    fecha = models.DateField(null=True)


class Seccion(models.Model):
    class Meta:
        verbose_name_plural = "Secciones" ## TIP ver arriba

    nombre = models.CharField(max_length=30)
