from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

def adminsignup(request):
	if request.method == "POST":
		un=request.POST.get("un")
		pw1=request.POST.get("pw1")
		pw2=request.POST.get("pw2")
		if pw1 == pw2:
			try:
				usr = User.objects.get(username=un)
				return render(request,"adminsignup.html",{"msg":"user already exists"})
			except User.DoesNotExist:
				usr = User.objects.create_user(username=un,password=pw1)
				usr.save()
				return redirect("adminlogin")
		else:
			return render(request,"adminsignup.html",{"msg":"password did not match"})
	else:
		return render(request,"adminsignup.html")

def adminlogin(request):
	if request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		usr = authenticate(username=un,password=pw)

		if usr is None:
			return render(request,"adminlogin.html",{"msg":"invalid login"})
		else:
			login(request,usr)
			return redirect("adminhome")

	else:
		return render(request,"adminlogin.html")

def userlogout(request):
	logout(request)
	return redirect("home")
