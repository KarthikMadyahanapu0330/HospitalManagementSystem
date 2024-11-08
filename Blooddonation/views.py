from django.shortcuts import render,redirect
from .models import BloodDonation

# Create your views here.
def blooddonation(request):
    if request.method == 'POST':
        donor_name = request.POST['donorName']
        date_of_donation = request.POST['dateofdonation']
        gender = request.POST['gender']
        age = request.POST['age']
        contact_info = request.POST['contactInfo']
        blood_type = request.POST['group']

        # Create a new BloodDonation object and save it to the database
        BloodDonation.objects.create(
            donor_name=donor_name,
            date_of_donation=date_of_donation,
            gender=gender,
            age=age,
            contact_info=contact_info,
            blood_type=blood_type
        )
    
        return render(request,'Blooddonation/Blooddonation.html',{'msg':'succesfull register for donation'})
    return render(request, 'Blooddonation/Blooddonation.html')
