# Generated by Django 5.0 on 2024-04-04 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserInterface', '0002_someothermodel_remove_slotbooking_doctor_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SlotBooking',
        ),
        migrations.DeleteModel(
            name='SomeOtherModel',
        ),
    ]
