# Generated by Django 5.1.4 on 2025-01-11 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muzeum_app', '0007_exhibit_end_date_exhibit_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit',
            name='start_date',
            field=models.DateField(),
        ),
    ]
