from django.contrib import admin
from home.models import Patients
from home.models import PatientsRation
from home.models import Kit
# Register your models here.
admin.site.register(Patients)
admin.site.register(PatientsRation)
admin.site.register(Kit)

