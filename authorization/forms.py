from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import User, Avatar


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2', 'first_name', 'last_name']

class UserEditForm(UserChangeForm):
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control col-md-6'}))
    last_name = forms.CharField(max_length=100, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control col-md-6'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        help_texts = {k:"" for k in fields}

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña actual', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(label='Contraseña nueva', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(label='Confirme contraseña', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):

    imagen = forms.ImageField(label="Imagen", required=False)

    class Meta:
        model = Avatar
        fields = ['imagen']