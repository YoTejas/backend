# Generated by Django 5.0.6 on 2024-06-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_merge_20240608_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='propertyStatus',
            field=models.CharField(choices=[('SOLD', 'SOLD'), ('UNDER_CONSTRUCTION', 'UNDER_CONSTRUCTION'), ('AVAILABLE', 'AVAILABLE')], default='AVAILABLE', max_length=255),
        ),
    ]