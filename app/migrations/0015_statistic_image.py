# Generated by Django 5.0.6 on 2024-06-08 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='statistics/'),
        ),
    ]
