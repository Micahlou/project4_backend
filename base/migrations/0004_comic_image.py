# Generated by Django 4.0.2 on 2022-02-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_comic_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='image',
            field=models.URLField(default='Image URL', verbose_name='Image URL'),
            preserve_default=False,
        ),
    ]