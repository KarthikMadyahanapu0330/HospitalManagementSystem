from django. urls import path
from . import views


urlpatterns =[
    path('mybookings/',views.mybookings,name='my_bookings'),
]