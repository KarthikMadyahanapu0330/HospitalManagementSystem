# Generated by Django 5.0 on 2024-03-27 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slotbooking', '0009_rename_booking_date_slotbooking_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slotbooking',
            old_name='booking',
            new_name='booking_date',
        ),
    ]
