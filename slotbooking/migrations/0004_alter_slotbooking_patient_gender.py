# Generated by Django 5.0 on 2024-03-19 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slotbooking', '0003_alter_slotbooking_patient_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slotbooking',
            name='patient_gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female'), ('o', 'others')], max_length=6),
        ),
    ]
