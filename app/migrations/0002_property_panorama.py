# Generated by Django 5.0.6 on 2024-05-24 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='panorama',
            field=models.FileField(blank=True, null=True, upload_to='panoramas/'),
        ),
    ]
