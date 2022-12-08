# Generated by Django 4.1.4 on 2022-12-08 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authh', '0004_remove_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('DoNotShow', 'do not show')], default=1, max_length=9),
            preserve_default=False,
        ),
    ]
