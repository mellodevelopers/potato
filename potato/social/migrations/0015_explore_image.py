# Generated by Django 3.0.3 on 2020-03-18 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0014_auto_20200318_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='explore',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hashtagpics'),
        ),
    ]
