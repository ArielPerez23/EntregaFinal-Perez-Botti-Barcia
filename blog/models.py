from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext as _

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(TimestampedModel, models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    state = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name 
    
class Curiosidades(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
