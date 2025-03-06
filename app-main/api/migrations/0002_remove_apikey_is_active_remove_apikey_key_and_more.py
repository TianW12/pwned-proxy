# Generated by Django 5.1.6 on 2025-03-06 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apikey',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='apikey',
            name='key',
        ),
        migrations.AddField(
            model_name='apikey',
            name='domain_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_keys', to='auth.group'),
        ),
        migrations.AddField(
            model_name='apikey',
            name='hashed_key',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True),
        ),
    ]
