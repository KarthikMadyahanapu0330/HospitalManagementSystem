# Generated by Django 5.0 on 2024-04-06 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slotbooking', '0010_rename_booking_slotbooking_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='slotbooking',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
