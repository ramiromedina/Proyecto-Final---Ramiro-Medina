from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TazasFormulario(forms.Form):
    categoria=forms.CharField(max_length=60)
    nombre=forms.CharField(max_length=60)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    informacion = forms.CharField(max_length=600)
    colores = forms.CharField(max_length=60)
    imagenTaza = forms.CharField(max_length=500)

class FunkosFormulario(forms.Form):
    categoria=forms.CharField(max_length=60)
    nombre=forms.CharField(max_length=60)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    informacion = forms.CharField(max_length=600)
    imagenFunko = forms.CharField(max_length=500)

class RemerasFormulario(forms.Form):
    categoria=forms.CharField(max_length=60)
    nombre=forms.CharField(max_length=60)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    talle = forms.CharField(max_length=60)
    imagenRemera = forms.CharField(max_length=500)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']