from django import forms

class NuevaPublicacion(forms.Form):
    titulo=forms.CharField(max_length=150)
    contenido=forms.CharField()