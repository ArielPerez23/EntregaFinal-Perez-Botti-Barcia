# Generated by Django 4.0.5 on 2022-07-21 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_article_author_alter_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
