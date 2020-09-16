# Generated by Django 3.1.1 on 2020-09-15 19:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Debe introducir dos caracteres')]),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='clase',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Debe introducir dos caracteres')]),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='destino',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Debe introducir dos caracteres')]),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='estado',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Debe introducir dos caracteres')]),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='origen',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Debe introducir dos caracteres')]),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='tipo_vuelo',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Debe introducir dos caracteres')]),
        ),
    ]
