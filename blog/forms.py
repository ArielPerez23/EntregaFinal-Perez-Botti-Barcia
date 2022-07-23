from django import forms
from django.forms import ModelForm
from .models import Article

# choices = [('Curiosidades','Curiosity'),('Software','Software'),('Hardware','Hardware')]

# class NewArticle(forms.Form):
    
#     title = forms.CharField(label='Titulo', max_length=150)
#     subtitle = forms.CharField(label='Subtitulo', max_length=200, required=False)
#     body = forms.CharField(label='Contenido', widget=forms.Textarea)
#     image = forms.ImageField(label='Imagen', required=False)
#     category = forms.ChoiceField(label='Categoria', choices=choices)

class NewArticle(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'