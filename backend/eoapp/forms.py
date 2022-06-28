from django.forms import ModelForm
from .models import Kit
from .models import Patients
from .models import PatientsRation

class KitForm(ModelForm):
	class Meta:
		model = Kit
		fields = ["no","name"]

class PatientsForm(ModelForm):
	class Meta:
		model = Patients
		fields = ["uid","name","father","mother"]

class PatientsRationForm(ModelForm):
	class Meta:
		model = PatientsRation
		fields = ["name","uid"]
