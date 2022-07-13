from email.mime import image
from django import forms

class NewArticle(forms.Form):
    
    title = forms.CharField(label='Titulo', max_length=150)
    subtitle = forms.CharField(label='Subtitulo', max_length=200, required=False)
    body = forms.CharField(label='Contenido', widget=forms.Textarea)
    image = forms.ImageField(label='Imagen', required=False)
