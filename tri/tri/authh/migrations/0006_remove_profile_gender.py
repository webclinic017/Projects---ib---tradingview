# Generated by Django 4.1.4 on 2022-12-09 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authh', '0005_profile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
    ]
