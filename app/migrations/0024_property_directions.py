# Generated by Django 5.0.6 on 2024-06-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_headermedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='directions',
            field=models.URLField(blank=True, null=True),
        ),
    ]