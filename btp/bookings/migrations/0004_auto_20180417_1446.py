# Generated by Django 2.0.4 on 2018-04-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20180407_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='available_seats',
            field=models.IntegerField(default=40),
        ),
        migrations.AlterField(
            model_name='status',
            name='booked_seats',
            field=models.IntegerField(default=0),
        ),
    ]
