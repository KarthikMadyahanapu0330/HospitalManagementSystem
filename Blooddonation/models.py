from django.db import models

# Create your models here.
class BloodDonation(models.Model):
    donor_name = models.CharField(max_length=255)
    date_of_donation = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    contact_info = models.CharField(max_length=255)
    BLOOD_GROUP_CHOICES = [
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    blood_type = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)


