# Generated by Django 5.0.6 on 2024-07-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_home_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='ph',
        ),
        migrations.AddField(
            model_name='login',
            name='user_name',
            field=models.CharField(default='default_username', max_length=50),
        ),
    ]
