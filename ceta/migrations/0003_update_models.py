from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('ceta', '0002_remove_user_user_ptr_alter_ceta_users_list_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.AddField(
            model_name='Client',
            name = 'is_active',
            field= models.BooleanField(default=True)
        ),
        migrations.AddField(
            model_name='Contract',
            name = 'is_active',
            field= models.BooleanField(default=True)
        ),
        migrations.AddField(
            model_name='PaymentEmployee',
            name = 'is_active',
            field= models.BooleanField(default=True)

        ),
        migrations.AddField(
            model_name='PaymentTerm',
            name = 'is_active',
            field= models.BooleanField(default=True)
        )
    ]