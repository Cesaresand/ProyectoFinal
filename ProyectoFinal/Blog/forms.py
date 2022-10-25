from django import forms


class ArticuloForm(forms.Form):

    titulo = forms.CharField(max_length=30)
    texto = forms.CharField(max_length=1500)
    fecha = forms.DateField()  ## tambien puede ir (required=False)


class AutorForm(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    profesion = forms.CharField(max_length=30)


class SeccionForm(forms.Form):

    seccion = forms.CharField(max_length=30)
    texto = forms.CharField(max_length=1500)
    autor = forms.CharField(max_length=30)
