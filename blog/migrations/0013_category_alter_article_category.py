# Generated by Django 4.0.5 on 2022-07-20 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_article_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Software', 'Software'), ('Hardware', 'Hardware'), ('Curiosidades', 'Curiosity')], max_length=30),
        ),
    ]
