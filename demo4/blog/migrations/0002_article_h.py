# Generated by Django 2.2.2 on 2019-06-13 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='h',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
