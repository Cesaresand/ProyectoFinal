from django.contrib import admin
from Blog.models import Articulo, Autor, Seccion, Avatar, Pagina

# Register your models here.

admin.site.register(Articulo)
admin.site.register(Autor)
admin.site.register(Seccion)
admin.site.register(Avatar)
admin.site.register(Pagina)
