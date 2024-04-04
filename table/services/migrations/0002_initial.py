# Generated by Django 4.2.9 on 2024-02-11 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='user_services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_services', to=settings.AUTH_USER_MODEL),
        ),
    ]
