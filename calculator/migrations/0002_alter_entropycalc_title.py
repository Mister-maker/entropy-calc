# Generated by Django 4.0.3 on 2022-03-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entropycalc',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]