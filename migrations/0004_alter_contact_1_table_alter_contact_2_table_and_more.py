# Generated by Django 5.0.6 on 2024-07-19 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0003_contact_1_contact_3'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='contact_1',
            table='Contact',
        ),
        migrations.AlterModelTable(
            name='contact_2',
            table='Register',
        ),
        migrations.AlterModelTable(
            name='contact_3',
            table='Customer',
        ),
    ]
