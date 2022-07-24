from django import forms
from django.forms import ModelForm

from authorization.forms import *

from .models import Article, Comment

class NewArticle(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    pasword2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    class Meta:
    
        model = User
        fields = ('__all__')
    
        help_texts = {k:"" for k in fields}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields  = ('name', 'text')

        widgets = {
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Text':forms.Textarea(attrs={'class':'form-control'}),
        }
