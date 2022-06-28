from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Kit
from .forms import KitForm
from .forms import PatientsForm
from .forms import PatientsRationForm
from .models import Patients
from .models import PatientsRation
import random 


def home(request):
	return render (request,"home.html")

def adminhome(request):
	if request.user.is_authenticated:
		return render(request,"adminhome.html")
	else:
		return redirect("adminlogin")

def patienthome(request):
	if request.user.is_authenticated:
		return render(request,"patienthome.html")
	else:
		return redirect("patientlogin")

def kit(request):
	if request.method == 'POST':
		user = request.user
		f = KitForm(request.POST)
		if f.is_valid():
			kitinfo = f.save(commit=False)
			# kitinfo.kit_id=random.randint(1,1000000)
			kitinfo.user = user
			kitinfo.save()
			fm = KitForm()
			data = Kit.objects.filter(user=request.user)
			return render(request, 'kit.html', {'fm': fm,'data' : data,'msg': 'Task Added'})
		else:
			return render(request, 'kit.html', {'fm': fm,'msg': 'Check Errors'})
	else:
		fm = KitForm()
		return render(request, 'kit.html', {'fm': fm})
	

def patients(request):
	if request.method == 'POST':
		user = request.user
		f = PatientsForm(request.POST)
		if f.is_valid():
			patientinfo = f.save(commit=False)
			patientinfo.user = user
			patientinfo.save()
			fmm = PatientsForm()
			data = Patients.objects.filter(user=request.user)
			return render(request, 'patients.html', {'fmm': fmm,'data' : data,'msg': 'Task Added'})
		else:
			return render(request, 'patients.html', {'fmm': fmm,'msg': 'Check Errors'})
	else:
		fmm = PatientsForm()
		return render(request, 'patients.html', {'fmm': fmm})

	
def patientration(request):
	if request.method == 'POST':
		user = request.user
		f = PatientsRationForm(request.POST)
		if f.is_valid():
			prationinfo = f.save(commit=False)
			prationinfo.user = user
			prationinfo.save()
			fmmm = PatientsRationForm()
			data = PatientsRation.objects.filter(user=request.user)
			return render(request, 'patientration.html', {'fmmm': fmmm,'data' : data,'msg': 'Task Added'})
		else:
			return render(request, 'patientration.html', {'fmmm': fmmm,'msg': 'Check Errors'})
	else:
		fmmm = PatientsRationForm()
		return render(request, 'patientration.html', {'fmmm': fmmm})
	