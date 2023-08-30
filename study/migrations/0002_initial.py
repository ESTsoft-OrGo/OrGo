# Generated by Django 4.2.4 on 2023-08-30 02:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_leader', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='study',
            name='participants',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_participants', to=settings.AUTH_USER_MODEL),
        ),
    ]