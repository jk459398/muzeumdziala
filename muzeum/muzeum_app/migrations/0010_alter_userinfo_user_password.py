# Generated by Django 5.1.4 on 2025-01-18 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muzeum_app', '0009_userinfo_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_password',
            field=models.CharField(default='default_password', max_length=255),
        ),
    ]
