from tabnanny import verbose
from django.db import models
from django.forms import model_to_dict
from django.utils.translation import gettext as _
from blog.constants import CATEGORY

class TimestampedModel(models.Model):
    '''
    Modelo de auditoria y control de cambios
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Avatar(TimestampedModel, models.Model):
    pass

class Image(TimestampedModel, models.Model):
    pass

class User(TimestampedModel, models.Model):
    pass

class Article(TimestampedModel, models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200,
                                    null=True, blank=True)
    body = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE,
                                    null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True) #Blank y null estan puestos aca porque me tiraba error en el form
    category = models.CharField(max_length=30, choices=CATEGORY)


