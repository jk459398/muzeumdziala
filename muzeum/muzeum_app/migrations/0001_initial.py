# Generated by Django 5.1.4 on 2025-01-11 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eksponat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod', models.CharField(max_length=20, unique=True)),
                ('tytul', models.CharField(max_length=100)),
                ('typ', models.CharField(max_length=50)),
                ('wysokosc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('szerokosc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('waga', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
