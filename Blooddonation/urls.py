from django. urls import path
from . import views



urlpatterns =[
    path('blooddonation/',views.blooddonation,name='blood_donation'),
]