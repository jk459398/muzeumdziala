# Generated by Django 5.1.4 on 2025-01-11 19:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muzeum_app', '0005_galeria_wypożyczenie'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Galeria',
            new_name='Gallery',
        ),
        migrations.RemoveField(
            model_name='wypożyczenie',
            name='Galeria',
        ),
        migrations.RenameModel(
            old_name='Artysta',
            new_name='Artist',
        ),
        migrations.RenameModel(
            old_name='Rozmiar',
            new_name='Size',
        ),
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('exhibit_code', models.CharField(max_length=100, unique=True)),
                ('type', models.CharField(max_length=100)),
                ('is_in_museum', models.BooleanField(default=True)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='muzeum_app.artist')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzeum_app.size')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=200)),
                ('institution_city', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzeum_app.exhibit')),
            ],
        ),
        migrations.DeleteModel(
            name='Eksponat',
        ),
        migrations.DeleteModel(
            name='Wypożyczenie',
        ),
    ]
