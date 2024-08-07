# Generated by Django 5.0.6 on 2024-07-08 09:59

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0002_client_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentUser',
            fields=[
            ],
            options={
                'verbose_name': 'Agent User',
                'verbose_name_plural': 'Agent Users',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ClientUser',
            fields=[
            ],
            options={
                'verbose_name': 'Client User',
                'verbose_name_plural': 'Client Users',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='approved',
        ),
    ]
