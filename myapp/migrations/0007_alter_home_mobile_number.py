# Generated by Django 5.0.6 on 2024-07-05 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='mobile_number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
