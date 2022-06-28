from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Kit
from .forms import KitForm
from .forms import PatientsForm
from .models import Patients
import random 



# Create your views here.
def index(request):
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
			return render(request, 'index.html', {'fm': fm,'data' : data,'msg': 'Task Added'})
		else:
			return render(request, 'index.html', {'fm': fm,'msg': 'Check Errors'})
	else:
		fm = KitForm()
		return render(request, 'index.html', {'fm': fm})

def about(request):
    #return HttpResponse("This is about page")
    return render(request,'about.html')

# def contact(request):
#     #return HttpResponse("This is contact page")
#     if(request.method == 'POST'):
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         pno = request.POST.get('pno')
#         desc = request.POST.get('desc')
#         date = datetime.today()
#         contact = Contact(name=name, email=email, pno=pno, desc=desc)
#         contact.save()
#     return render(request,'contact.html')

def services(request):
    #return HttpResponse("This is services page")

    return render(request,'services.html')


# def patients(request):
#     if(request.method == 'POST'):
#         uid = request.POST.get('uid')
#         name = request.POST.get('name')
#         father = request.POST.get('father')
#         mother = request.POST.get('mother')
#         patients = Patients(uid=uid, name=name, father=father, mother=mother)
#         patients.save()
#     return render(request, 'patient.html')

def pration(request):
	if request.method == 'POST':
		user = request.user
		f = PatientsForm(request.POST)
		if f.is_valid():
			prationinfo = f.save(commit=False)
			prationinfo.user = user
			prationinfo.save()
			fmm = PatientsForm()
			data = Patients.objects.filter(user=request.user)
			return render(request, 'index.html', {'fmm': fmm,'data' : data,'msg': 'Task Added'})
		else:
			return render(request, 'index.html', {'fmm': fmm,'msg': 'Check Errors'})
	else:
		fm = PatientsForm()
		return render(request, 'index.html', {'fmm': fmm})

def patient(request):
	if request.method == 'POST':
		user = request.user
		f = PatientsForm(request.POST)
		if f.is_valid():
			patientinfo = f.save(commit=False)
			patientinfo.user = user
			patientinfo.save()
			fmm = PatientsForm()
			data = Patients.objects.filter(user=request.user)
			return render(request, 'index.html', {'fmm': fmm,'data' : data,'msg': 'Task Added'})
		else:
			return render(request, 'index.html', {'fmm': fmm,'msg': 'Check Errors'})
	else:
		fm = PatientsForm()
		return render(request, 'index.html', {'fmm': fmm})














