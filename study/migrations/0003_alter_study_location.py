# Generated by Django 4.2.4 on 2023-08-24 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_remove_study_participants_study_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]