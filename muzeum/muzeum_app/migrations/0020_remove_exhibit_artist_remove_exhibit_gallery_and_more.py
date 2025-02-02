# Generated by Django 5.1.4 on 2025-02-01 00:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muzeum_app', '0019_alter_exhibit_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibit',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='exhibit',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='exhibit',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='exhibit',
            name='size',
        ),
        migrations.CreateModel(
            name='Eksponat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='muzeum_app.artist')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzeum_app.size')),
            ],
        ),
        migrations.AlterField(
            model_name='loan',
            name='exhibit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzeum_app.eksponat'),
        ),
        migrations.DeleteModel(
            name='LoanHistory',
        ),
        migrations.DeleteModel(
            name='Exhibit',
        ),
    ]
