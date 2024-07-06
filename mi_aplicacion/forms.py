from django import forms
from .models import Producto
from multiprocessing import AuthenticationError
from django.contrib.auth.models import User

class Usuario(forms.Form):
    nombre = forms.CharField(label= "Nombre", max_length=200)
    apellido = forms.CharField(label= "Apellido", max_length=200)
    correo = forms.EmailField(label= "Correo", max_length=200)
    contrasena = forms.CharField(label= "contraseña", max_length=200)
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'imagen', 'precio', 'categoria']


class LoginForm(forms.Form):
    correo = forms.CharField()
    contrasena = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        correo = cleaned_data.get('correo')
        contrasena = cleaned_data.get('contraseña')

        if not User.objects.filter(correo=correo).exists():
            raise forms.ValidationError("Este usuario no existe.")

        user = AuthenticationError(correo=correo, contrasena=contrasena)
        if user is None:
            raise forms.ValidationError("Usuario o contraseña incorrectos.")

        return cleaned_data