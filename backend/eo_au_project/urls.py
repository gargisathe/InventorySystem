
from django.contrib import admin
from django.urls import path
from eoapp.views import home,adminhome,patienthome
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
    path("patienthome/",patienthome,name="patienthome")
]
