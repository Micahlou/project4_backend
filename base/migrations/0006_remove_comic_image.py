# Generated by Django 4.0.2 on 2022-02-25 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_comic_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comic',
            name='image',
        ),
    ]
