# Generated by Django 4.0.2 on 2022-02-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_comic_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='image',
            field=models.URLField(default='https://i.imgur.com/ShzwUoR.png', verbose_name='https://i.imgur.com/ShzwUoR.png'),
            preserve_default=False,
        ),
    ]
