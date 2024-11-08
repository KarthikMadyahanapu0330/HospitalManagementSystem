from django.shortcuts import render
from .models import SlotBooking
from django.http import HttpResponse
from datetime import date


def slot_booking(request):
    today =date.today()
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        mobile = request.POST['mobile']
        booking = request.POST['date']
        timeslot = request.POST['timeslot']
        gender = request.POST['gender']
        SlotBooking.objects.create(
            patient_name=name,
            patient_age=age,
            patient_mobile=mobile,
            booking_date=booking,
            booking_time=timeslot,
            patient_gender=gender
        )
        return render(request, 'slot/slotbooking.html',{'msg':'slotbooked successfully','today':today})



    return render(request, 'slot/slotbooking.html',{'today':today}) 

