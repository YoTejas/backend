# Generated by Django 5.0.6 on 2024-05-21 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('locality', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('landmarkName', models.CharField(blank=True, max_length=255, null=True)),
                ('landmarkCoordinates', models.CharField(blank=True, max_length=255, null=True)),
                ('partialAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('completeAddress', models.TextField(blank=True, null=True)),
                ('rooms', models.CharField(blank=True, max_length=255, null=True)),
                ('area', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('amenities', models.ManyToManyField(blank=True, related_name='amenities', to='app.amenity')),
                ('images', models.ManyToManyField(blank=True, related_name='images', to='app.image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
