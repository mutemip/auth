# Generated by Django 4.1.5 on 2023-02-09 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='booking',
            table='booking',
        ),
        migrations.AlterModelTable(
            name='menu',
            table='menu',
        ),
    ]
