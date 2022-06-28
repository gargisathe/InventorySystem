from django.shortcuts import render,redirect


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
