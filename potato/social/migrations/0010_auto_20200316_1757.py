# Generated by Django 3.0.3 on 2020-03-16 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0009_auto_20200316_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='social.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.FileField(blank=True, null=True, upload_to='postpics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='typ',
            field=models.CharField(blank=True, default='', help_text='only video and image', max_length=5),
        ),
    ]
