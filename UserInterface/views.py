from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect
from django.http import HttpResponse
from .models import SlotBooking
from datetime import date
from django.http import HttpResponseRedirect




# Create your views here.
def ShowUserInterface(request):
    return render(request,'UserInterface/userinterface.html')

def patientlogin(request):
    return render(request,'patient login/patientlogin.html') 

def patientsignup(request):
    return render(request,'patient signup/patientsignup.html')

def dashboardpage(request):
    return render(request,'dashboard/dashboard.html')


def doctorlogin(request):
    return render(request,'doctorlogin/doctorlogin.html')

def doctorsignup(request):
    return render(request,'doctorlogin/doctorsignup.html')

def showdoctordashboard(request):
    today = date.today()
    upcoming_patients = SlotBooking.objects.filter(booking_date__gte=today)

    return render(request, 'doctordashboard/doctordashboard.html', {'upcoming_patients': upcoming_patients})

def complete_appointment(request,patient_id):
    slot_booking = SlotBooking.objects.get(patient_id=patient_id)
    slot_booking.completed = True
    slot_booking.save()
    upcoming_patients= SlotBooking.objects.filter(completed=False)
    previous_patients =SlotBooking.objects.filter(completed=True)
    return render(request, 'doctordashboard/doctordashboard.html',{'previous_patients':previous_patients,
                                                                   'upcoming_patients':upcoming_patients})
from .models import SlotBooking
def delete_patient(request,patient_id):
    patient= SlotBooking.objects.get(patient_id=patient_id)
    #patient = SlotBooking.objects.get(pk=patient_id)
    patient.delete()
   # previous_patient =SlotBooking.object.filter(completed=True)
    return redirect('doctor_dashboard')
