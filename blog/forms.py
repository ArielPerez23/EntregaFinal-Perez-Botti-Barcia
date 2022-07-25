from django import forms
from django.forms import ModelForm

from .models import Article, Comment

class NewArticle(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields  = ('name', 'text')

        widgets = {
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Text':forms.Textarea(attrs={'class':'form-control'}),
        }
