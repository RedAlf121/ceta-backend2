# Generated by Django 5.0.3 on 2024-08-28 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceta', '0005_client_email_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email_client',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
