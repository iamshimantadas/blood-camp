from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from core.models import *


def RegisterView(request):
    if request.method == "POST":
        data = request.POST

        firstname = data.get("first_name")
        lastname = data.get("last_name")
        email = data.get("email")
        password = data.get("password")
        phone = data.get("phone")
        address = data.get("address")
        # bloodgrp = data.get("blood_group")

        user = User.objects.create(
            first_name=firstname,
            last_name=lastname,
            email=email,
            address=address,
            phone=phone,
            # blood_group = bloodgrp,
            status=False,
            is_hospital_stff=True,
        )
        try:
            user.set_password(password)
            user.save()
            context = {"register_email": email, "register_password": password, "register_phone":phone}
            return render(request, "h_login.html", context)
        except Exception as e:
            print(e)
            return HttpResponse("error occured!")
    else:
        return render(request,"h_register.html")
    
    
def LoginView(request):
    if request.method == "POST":
        data = request.POST
        phone = data.get("phone")
        phone = int(phone)
        user = User.objects.get(email=data.get("email"))
        auth = authenticate(email=data.get("email"), password=data.get("password"))
        
        if auth:
            if phone == user.phone:
                login(request, user)
                return redirect("/ricipient/dashboard/")
            else:
                return HttpResponse("phone number not match! Please enter correct one!")
        else:
            return HttpResponse("please enter right credentials!")
    else:
        user = request.user
        if user.is_authenticated:
            if user.is_hospital_stff:
                acc_status = user.status
                context = {"status": acc_status}
                return render(request, "dashboard/h_dashboard.html", context)
            else:
                return render(request, "h_login.html")
        else:
            return render(request, "h_login.html")
        


def DashboardView(request):
    user = request.user
    if user.is_authenticated:
        acc_status = user.status
        context = {"status": acc_status}
        return render(request, "dashboard/h_dashboard.html", context)
    else:
        return redirect("/hospital/login/")


def InfoView(request):
    if request.method == "POST":
        data = request.POST

        firstname = data.get("first_name")
        lastname = data.get("last_name")
        email = data.get("email")
        password = data.get("password")
        phone = data.get("phone")
        address = data.get("address")
        blood_group = data.get("blood_group")

        user = User.objects.get(id=request.user.id)


        if firstname:
            user.first_name = firstname
            user.save()
        else:
            pass

        if lastname:
            user.last_name = lastname
            user.save()
        else:
            pass

        if email:
            user.email = email
            user.save()
        else:
            pass

        if address:
            user.address = address
            user.save()
        else:
            pass    

        if phone:
            user.phone = phone
            user.save()
        else:
            pass    


        if password:
            user.set_password(password)
            user.save()
            login(request, user)
        else:
            pass

        if blood_group:
            user.blood_group = blood_group
            user.save()
        else:
            pass

        return redirect("/hospital/login/")
    else:
        user = request.user
        if user.is_authenticated:
            user_obj = User.objects.get(email=user.email)
            print(user_obj)
            context = {"data": user_obj}
            return render(request, "dashboard/h_info.html", context)
        else:
            # return redirect("/login/")
            return redirect("/hospital/login/")


def LogoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")
    else:
        # return redirect("/login/")
        return redirect("/ricipient/login/")
