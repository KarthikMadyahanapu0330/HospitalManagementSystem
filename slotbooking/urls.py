from django.urls import path
from . import views

urlpatterns =[
    path('slotbooking',views.slot_booking,name='slot_booking')
]