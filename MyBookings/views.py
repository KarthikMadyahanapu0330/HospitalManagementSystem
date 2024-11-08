from django.shortcuts import render

# Create your views here.
def mybookings(request):
    return render (request,'mybookings/mybookings.html')