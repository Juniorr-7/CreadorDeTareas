# Generated by Django 5.0.2 on 2024-08-24 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=200)),
                ('estado', models.CharField(choices=[('finalizada', 'Finalizada'), ('incompleta', 'Incompleta')], default='incompleta', max_length=50)),
            ],
        ),
    ]
