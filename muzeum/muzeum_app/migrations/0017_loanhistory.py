# Generated by Django 5.1.4 on 2025-01-31 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muzeum_app', '0016_institution_alter_exhibit_status_exhibit_institution'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzeum_app.exhibit')),
            ],
        ),
    ]
