from django.contrib import admin
from eoapp.models import Patients
from eoapp.models import PatientsRation
from eoapp.models import Kit
# Register your models here.
admin.site.register(Patients)
admin.site.register(PatientsRation)
admin.site.register(Kit)

