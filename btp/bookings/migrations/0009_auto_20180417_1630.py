# Generated by Django 2.0.4 on 2018-04-17 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_auto_20180417_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='bus_id',
            new_name='bus',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='bus',
        ),
    ]
