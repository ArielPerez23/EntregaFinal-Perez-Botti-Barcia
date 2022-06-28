from django import forms

class CuriosidadesForm(forms.Form):
    titulo=forms.CharField()
    subtitulo=forms.CharField()
    contenido=forms.CharField()