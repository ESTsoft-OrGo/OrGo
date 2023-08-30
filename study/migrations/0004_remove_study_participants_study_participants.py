# Generated by Django 4.2.4 on 2023-08-30 04:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0003_alter_study_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study',
            name='participants',
        ),
        migrations.AddField(
            model_name='study',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='study_participants', to=settings.AUTH_USER_MODEL),
        ),
    ]