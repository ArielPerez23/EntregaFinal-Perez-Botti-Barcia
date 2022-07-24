from django.db import models
from django.utils.translation import gettext as _

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from blog.constants import *

from authorization.models import User

class TimestampedModel(models.Model):
    '''
    Modelo de auditoria y control de cambios
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Article(TimestampedModel, models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True,)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, editable=False) 
    category = models.CharField(max_length=30, choices=CATEGORY)
    likes = models.ManyToManyField(User, related_name='user_likes',blank=True, null=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

class Message(TimestampedModel, models.Model):
    sender = models.ManyToManyField(User, null=True, blank=True, related_name='sender_user')
    receiver = models.ManyToManyField(User, null=True, blank=True, related_name='receiver_user')
    message = models.TextField(max_length=255, null=True, blank=True)

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

