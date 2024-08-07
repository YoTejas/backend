# Generated by Django 5.0.6 on 2024-05-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_employee_facebooklink_employee_instagramlink_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('value', models.IntegerField(blank=True, null=True)),
                ('to_show', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
