# Generated by Django 4.0.3 on 2022-03-27 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0006_entropycalc_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entropycalc',
            name='output',
        ),
        migrations.RemoveField(
            model_name='entropycalc',
            name='url',
        ),
    ]
