# Generated by Django 4.2.5 on 2023-10-07 04:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]