from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Autor(models.Model):
    class Meta:
        verbose_name_plural = (
            "Autores"  # ESTO sirve para corregir el nombre de Autor TIP!
        )

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Profesión: {self.profesion} - Email: {self.email}"


class Articulo(models.Model):

    titulo = models.CharField(max_length=30)
    texto = models.CharField(max_length=1500)
    fecha = models.DateField(null=True)

    def __str__(self):
        return self.titulo


class Seccion(models.Model):
    class Meta:
        verbose_name_plural = "Secciones"  ## TIP ver arriba

    seccion = models.CharField(max_length=30)
    texto = models.CharField(max_length=1500)
    autor = models.CharField(max_length=30)

    def __str__(self):
        return self.seccion


##############################################################################


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)


class Pagina(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    texto = models.CharField(max_length=1000)
    fecha = models.DateField(null=True)

    def __str__(self):
        return self.titulo
