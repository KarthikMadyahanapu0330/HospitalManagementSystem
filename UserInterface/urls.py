from django.urls import path
from . import views

urlpatterns=[
    path('',views.ShowUserInterface),
    path('patientlogin/',views.patientlogin, name='patient_login'),
    path('patientsignup/',views.patientsignup,name='patient_signup'),
    path('dashboard/',views.dashboardpage,name='dash_board'),
    path('doctorlogin/',views.doctorlogin,name='doctor_login'),
    path('doctorsignup/',views.doctorsignup,name='doctor_signup'),
    path('doctordashboard/',views.showdoctordashboard,name='doctor_dashboard'),
    path('completeappointment/<int:patient_id>/',views.complete_appointment,name='complete_appointment'),
    path('deletepatient/<int:patient_id>/',views.delete_patient,name='delete_patient'),
    
]