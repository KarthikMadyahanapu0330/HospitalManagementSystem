from django.shortcuts import render, redirect
from .models import BloodTest
from django.http import HttpResponse
from datetime import date




# Create your views here.
def bloodtest(request):
    if request.method == 'POST':
        patient_name = request.POST['patientName']
        date_of_birth = request.POST['dateOfBirth']
        gender = request.POST['gender']
        age = request.POST['age']
        contact_info = request.POST['contactInfo']
        date_of_visit = request.POST['dateOfVisit']
        blood_group = request.POST['group']

        blood_test = BloodTest(
            patient_name=patient_name,
            date_of_birth=date_of_birth,
            gender=gender,
            age=age,
            contact_info=contact_info,
            date_of_visit=date_of_visit,
            blood_group=blood_group
        )
        blood_test.save()
        return render(request,'Bloodtest/bloodtest.html',{'msg':'Test slot successfully booked '})
    return render(request,'Bloodtest/bloodtest.html')

