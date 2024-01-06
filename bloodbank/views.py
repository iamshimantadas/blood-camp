from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from core.models import User


def LoginView(request):
    if request.method == "POST":
        data = request.POST
        email = data.get("email")
        password = data.get("password")

        user = authenticate(email=email, password=password)

        if user:
            user_obj = User.objects.get(email=user.email)
            login(request, user)
            # context = {"user": user_obj}
            # return render(request, "dashboard/bank_dashboard.html", context)
            return redirect("dashboard/")
        else:
            return HttpResponse("credentials not match!")
    else:
        user = request.user
        if user.is_authenticated:
            if user.is_authenticated:
                if user.is_superuser:
                    return render(request, "dashboard/bank_dashboard.html")
                else:
                    return render(request, "bank_login.html")
        else:
            return render(request, "bank_login.html")


def DashboardView(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            return render(request, "dashboard/bank_dashboard.html")
        else:
            return HttpResponse(
                "you are not an admin user! plz make correct login details!"
            )
    else:
        return HttpResponse(
            "you are not an admin user! plz make correct login details!"
        )


def DonorRequestView(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            user = User.objects.filter(is_donor=True, status=False)
            return render(
                request, "dashboard/donor_requests.html", context={"donor": user}
            )
        else:
            return HttpResponse("not an admin!")
    else:
        return redirect("login/")


def DonorAccountReview(request):
    user = request.user

    if user.is_authenticated:
        if user.is_superuser:
            if request.method == "POST":
                data = request.POST
                donor_id = data.get("donorid")
                # print(donor_id)
                if User.objects.filter(id=donor_id).exists():
                    user = User.objects.get(id=donor_id)
                    try:
                        user.status = True
                        user.save()

                        user = User.objects.filter(is_donor=True, status=False)
                        return render(
                            request,
                            "dashboard/donor_requests.html",
                            context={"donor": user},
                        )
                    except Exception as e:
                        print(e)
                        return HttpResponse("error occured!")
                else:
                    return HttpResponse("bad request!")
            else:
                return HttpResponse("bad request!")
        else:
            return HttpResponse("not an admin!")
    else:
        return redirect("login/")
    

def RicipientRequestView(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            user = User.objects.filter(is_receipient=True, status=False)
            return render(
                request, "dashboard/ricipients_requests.html", context={"ricipient": user}
            )
        else:
            return HttpResponse("not an admin!")
    else:
        return redirect("login/")


def RicipientAccountReview(request):
    user = request.user

    if user.is_authenticated:
        if user.is_superuser:
            if request.method == "POST":
                data = request.POST
                ricipient_id = data.get("ricipientid")
                # print(donor_id)
                if User.objects.filter(id=ricipient_id).exists():
                    user = User.objects.get(id=ricipient_id)
                    try:
                        user.status = True
                        user.save()

                        user = User.objects.filter(is_receipient=True, status=False)
                        return render(
                            request,
                            "dashboard/ricipients_requests.html",
                            context={"ricipient": user},
                        )
                    except Exception as e:
                        print(e)
                        return HttpResponse("error occured!")
                else:
                    return HttpResponse("bad request!")
            else:
                return HttpResponse("bad request!")
        else:
            return HttpResponse("not an admin!")
    else:
        return redirect("login/")    




def HospitalRequestView(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            user = User.objects.filter(is_hospital_stff=True, status=False)
            return render(
                request, "dashboard/hospital_staff_requests.html", context={"hospital": user}
            )
        else:
            return HttpResponse("not an admin!")
    else:
        return redirect("login/")


def HospitalAccountReview(request):
    user = request.user

    if user.is_authenticated:
        if user.is_superuser:
            if request.method == "POST":
                data = request.POST
                staff_id = data.get("staffid")
              
                if User.objects.filter(id=staff_id).exists():
                    user = User.objects.get(id=staff_id)
                    try:
                        user.status = True
                        user.save()

                        user = User.objects.filter(is_hospital_stff=True, status=False)
                        return render(
                            request,
                            "dashboard/hospital_staff_requests.html",
                            context={"hospital": user},
                        )
                    except Exception as e:
                        print(e)
                        return HttpResponse("error occured!")
                else:
                    return HttpResponse("bad request!")
            else:
                return HttpResponse("bad request!")
        else:
            return HttpResponse("not an admin!")
    else:
        return redirect("login/")     