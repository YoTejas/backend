# Generated by Django 5.0.6 on 2024-06-21 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_values_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='contact',
            new_name='name',
        ),
        migrations.AddField(
            model_name='message',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='role',
            field=models.CharField(choices=[('client', 'client'), ('agent', 'agent')], default='client', max_length=255),
        ),
    ]