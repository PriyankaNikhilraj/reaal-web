# Generated by Django 5.0.6 on 2024-07-03 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_login_ph'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=15)),
                ('member_id', models.CharField(max_length=50)),
                ('left_customer', models.IntegerField(default=0)),
                ('right_customer', models.IntegerField(default=0)),
                ('amount', models.FloatField(default=0)),
                ('rebirth', models.BooleanField(default=False)),
                ('income', models.FloatField(default=0)),
                ('count', models.IntegerField()),
                ('si_no', models.IntegerField()),
                ('formatted_date', models.CharField(max_length=20)),
            ],
        ),
    ]
