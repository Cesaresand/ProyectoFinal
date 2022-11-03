from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Blog.models import Avatar


class ArticuloForm(forms.Form):

    titulo = forms.CharField(max_length=30)
    texto = forms.CharField(max_length=1500)
    fecha = forms.DateField()  ## tambien puede ir (required=False)


class AutorForm(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    profesion = forms.CharField(max_length=30)
    email = forms.EmailField()


class SeccionForm(forms.Form):

    seccion = forms.CharField(max_length=30)
    texto = forms.CharField(max_length=1500)
    autor = forms.CharField(max_length=30)


#################################################################################################


class UserEditionForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}


class AvatarForm(forms.ModelForm):

    imagen = forms.ImageField()

    class Meta:
        model = Avatar
        fields = ["imagen", "user"]
