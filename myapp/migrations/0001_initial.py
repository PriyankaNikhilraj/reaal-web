# Generated by Django 5.0.6 on 2024-07-02 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph', models.IntegerField(max_length=15)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
