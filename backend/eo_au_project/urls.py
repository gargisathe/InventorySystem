
from django.contrib import admin
from django.urls import path
from eoapp.views import home,adminhome,patienthome,kit,patients,patientration
from auapp.views import adminlogin,userlogout,adminsignup
from aupatient.views import patientlogin,patientsignup


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("adminlogin/",adminlogin,name="adminlogin"),
    path("adminsignup/",adminsignup,name="adminsignup"),
    path("adminhome/",adminhome,name="adminhome"),
    path("userlogout/",userlogout,name="userlogout"),
    path("patientsignup/",patientsignup,name="patientsignup"),
    path("patientlogin/",patientlogin,name="patientlogin"),
    path("patienthome/",patienthome,name="patienthome"),
    path("kit/",kit,name="kit"),
    path("patients/",patients,name="patients"),
    path("patientration/",patientration,name="patientration"),
]
