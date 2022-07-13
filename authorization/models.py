import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .managers import UserManager

class User(AbstractUser):
    '''
    Custom User Model validando el campo de USERNAME con el email    
    '''
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(_('email address'), unique=True)
    objects = UserManager()


# Funcion para definir un usuario random para el modelo.
def random_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = uuid.uuid4().hex[:30]

# Signals
models.signals.pre_save.connect(random_username, sender=User)