# Generated by Django 3.0.3 on 2020-03-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20200312_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explore',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
