from django.db import models
from datetime import date

# Create your models here.
class SlotBooking(models.Model):
    gender_choices =[
        ('m','male'),
        ('f','female'),
        ('o','others'),
    ]
    patient_id = models.IntegerField(primary_key=True)
    patient_name = models.CharField(max_length=50)
    patient_age = models.IntegerField(default=0)
    patient_mobile = models.CharField(max_length=15,unique=True)
    booking_date = models.DateField(default=date.today)
    booking_time = models.CharField(max_length=20)
    patient_gender = models.CharField(max_length=6, choices=gender_choices)
    completed = models.BooleanField(default=False)  # Add this field



    def save(self, *args, **kwargs):
        if not self.pk:  
            last_id = SlotBooking.objects.order_by('-patient_id').first()
            if last_id:
                self.patient_id = last_id.patient_id + 1
            else:
                self.patient_id = 100  
        super().save(*args, **kwargs)