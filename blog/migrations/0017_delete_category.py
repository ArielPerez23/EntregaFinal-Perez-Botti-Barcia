# Generated by Django 4.0.5 on 2022-07-23 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_article_category_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
