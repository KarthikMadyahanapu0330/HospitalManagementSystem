from django . urls import path
from . import views


urlpatterns =[
    path('bloodtest/',views.bloodtest,name='blood_test'),
]