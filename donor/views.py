from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from core.models import User, Bloodstock, Blooddonation


def RegisterView(request):
    if request.method == "POST":
        data = request.POST

        firstname = data.get("first_name")
        lastname = data.get("last_name")
        email = data.get("email")
        password = data.get("password")
        phone = data.get("phone")
        address = data.get("address")
        bloodgrp = data.get("blood_group")

        blood_obj = Bloodstock.objects.get(id=bloodgrp)

        user = User.objects.create(
            first_name=firstname,
            last_name=lastname,
            email=email,
            address=address,
            phone=phone,
            blood_group = blood_obj,
            status=False,
            is_donor=True,
        )
        try:
            user.set_password(password)
            user.save()
            context = {"register_email": email, "register_password": password, "register_phone":phone}
            return render(request, "login.html", context)
        except Exception as e:
            print(e)
            return HttpResponse("error occured!")
    else:
        stock = Bloodstock.objects.all()
        context = {"stock":stock}
        return render(request, "register.html",context)


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
                return redirect("/donor/d_dashboard/")
            else:
                return HttpResponse("phone number not match! Please enter correct one!")
        else:
            return HttpResponse("please enter right credentials!")
    else:
        user = request.user
        if user.is_authenticated:
            if user.is_donor:
                acc_status = user.status
                context = {"status": acc_status}
                return render(request, "dashboard/dashboard.html", context)
            else:
                return render(request, "login.html")
        else:
            return render(request, "login.html")


def DashboardView(request):
    user = request.user
    if user.is_authenticated:
            if user.is_donor:
                acc_status = user.status
                try:
                    stock = Bloodstock.objects.get(quantity=0)
                    user_obj = User.objects.get(id=request.user.id)
                    donation = Blooddonation.objects.filter(donate_userid=user_obj).exists()
                    # print("donation: ",donation)
                    if donation:
                        stock=None
                        if stock==user.blood_group:
                            context = {"status": acc_status,"blood_group":user.blood_group}
                            return render(request, "dashboard/dashboard.html", context)
                        else:
                            context = {"status": acc_status}
                            return render(request, "dashboard/dashboard.html", context)
                    else:
                        if stock==user.blood_group:
                            context = {"status": acc_status,"blood_group":user.blood_group}
                            return render(request, "dashboard/dashboard.html", context)
                        else:
                            context = {"status": acc_status}
                            return render(request, "dashboard/dashboard.html", context)
                
                except Exception as e:
                    print(e)    
                    context = {"status": acc_status}
                    return render(request, "dashboard/dashboard.html", context)
            else:
                return render(request, "login.html")
    else:
        return redirect("/donor/d_login/")


def InfoView(request):
    if request.method == "POST":
        data = request.POST

        firstname = data.get("first_name")
        lastname = data.get("last_name")
        email = data.get("email")
        password = data.get("password")
        bloodgrpid = data.get("blood_group")
        phone = data.get("phone")
        address = data.get("address")

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

        if bloodgrpid:
            if Bloodstock.objects.filter(id=bloodgrpid).exists():
                stock_obj = Bloodstock.objects.get(id=bloodgrpid)
                user.blood_group = stock_obj
                user.save()
            else:
                pass
            
        else:
            pass
        return redirect("/donor/d_login/")
    else:
        user = request.user
        if user.is_authenticated:
            if user.is_donor:
                user_obj = User.objects.get(email=user.email)
                stock = Bloodstock.objects.all()
                context = {"data": user_obj,"stock":stock}
                return render(request, "dashboard/info.html", context)
            else:
                return HttpResponse("bad request")
        else:
            return redirect("/donor/d_login/")


def LogoutView(request):
    user = request.user
    if request.user.is_authenticated:
        if user.is_donor:
            logout(request)
            return redirect("/donor/d_login/")
        else:
            return HttpResponse("you are a donor!")
    else:
        return redirect("/donor/d_login/")


def DonateBloodView(request):
    user = request.user
    if request.user.is_authenticated:
        if user.is_donor:
            if request.method == "POST":
                data = request.POST

                userid = data.get("userid")
                userid = int(userid)
                user_obj = User.objects.get(id=userid)
                symptom = data.get("bodySymptom")
                
                try:
                    donate = Blooddonation.objects.create(
                    donate_userid = user_obj,
                    donate_date = data.get("bloodDonationDate"),
                    donate_time = data.get("donationTime"),
                    )
                    if symptom:
                        donate.disease = symptom
                        donate.save()
                        return redirect("/donor/d_login/")
                    else:
                        donate.disease = None
                        donate.save()
                        return redirect("/donor/d_login/")
                    
                    
                except Exception as e:
                    print(e)
                    return HttpResponse("error occured!")
            else:
                context = {"userid":request.user.id}
                return render(request,"dashboard/donate.html",context)
        else:
            return HttpResponse("you are a donor!")
    else:
        return redirect("/donor/d_login/")