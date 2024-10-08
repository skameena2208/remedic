# Generated by Django 5.0.6 on 2024-07-19 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0002_contact_2_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
            ],
        ),
    ]
