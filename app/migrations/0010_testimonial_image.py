# Generated by Django 4.2.13 on 2024-06-03 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='testimonials/'),
        ),
    ]
