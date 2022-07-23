# Generated by Django 4.0.5 on 2022-07-23 22:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0017_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(related_name='user_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
