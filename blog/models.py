from django.db import models
from django.utils.translation import gettext as _

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from authorization.models import User

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
    '''
    Model para imagenes de Avatares de usuarios
    '''
    pass

class UserProfile(models.Model):
    '''
    Model para el perfil de cada usuario.
    '''
    # 
    # bio =
    # 

    pass

class Article(TimestampedModel, models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True,)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, editable=False) #Blank y null estan puestos aca porque me tiraba error en el form
    category = models.CharField(max_length=30, choices=CATEGORY)



### Dejar al final del codigo ###
@receiver(pre_save, sender=Article)
def set_author(sender, instance, *args, **kwargs):
    '''
    Signal para asignacion automatica de Article Author 
    '''
    import inspect
    for frame_record in inspect.stack():
        if frame_record[3]=='get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None
    
    if request:
        instance.author = request.user

    
