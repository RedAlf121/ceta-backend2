# Generated by Django 5.0.3 on 2024-08-28 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceta', '0003_update_models'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='email_client',
        ),
    ]
