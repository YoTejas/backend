# Generated by Django 5.0.6 on 2024-06-14 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_remove_property_locality'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='locality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='properties', to='app.locality'),
        ),
    ]
