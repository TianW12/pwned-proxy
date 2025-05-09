# Generated by Django 5.1.6 on 2025-03-25 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_apikey_is_active_remove_apikey_key_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='apikey',
            old_name='domain_group',
            new_name='group',
        ),
        migrations.RemoveField(
            model_name='apikey',
            name='allowed_domain',
        ),
        migrations.AddField(
            model_name='apikey',
            name='domains',
            field=models.ManyToManyField(blank=True, to='api.domain'),
        ),
    ]
