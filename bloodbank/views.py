from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from core.models import User, Bloodstock, Order, Offlinedelivery


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
        return redirect("/bank_admin/")


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
        return redirect("/bank_admin/")


def RicipientRequestView(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            user = User.objects.filter(is_receipient=True, status=False)
            return render(
                request,
                "dashboard/ricipients_requests.html",
                context={"ricipient": user},
            )
        else:
            return HttpResponse("not an admin!")
    else:
        return redirect("/bank_admin/")


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
        return redirect("/bank_admin/")


def HospitalRequestView(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            user = User.objects.filter(is_hospital_stff=True, status=False)
            return render(
                request,
                "dashboard/hospital_staff_requests.html",
                context={"hospital": user},
            )
        else:
            return HttpResponse("not an admin!")
    else:
        return redirect("/bank_admin/")


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
        return redirect("/bank_admin/")


def BloodStockView(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            stock = Bloodstock.objects.all()
            return render(
                request, "dashboard/blood_stock.html", context={"blood": stock}
            )
        else:
            return redirect("/bank_admin/")
    else:
        return redirect("/bank_admin/")


def AddBloodGroupView(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            if request.method == "POST":
                data = request.POST
                if Bloodstock.objects.filter(blood_type=data.get("bloodname")).exists():
                    return HttpResponse("Blood Group Type already exist!")
                else:
                    try:
                        blood_obj = Bloodstock.objects.create(
                            blood_type=data.get("bloodname"), quantity=False
                        )
                        blood_obj.save()
                    except Exception as e:
                        print(e)
                        return HttpResponse("error occured!")

                    stock = Bloodstock.objects.all()
                    return render(
                        request, "dashboard/blood_stock.html", context={"blood": stock}
                    )
            else:
                return HttpResponse("bad request!")
        else:
            return redirect("/bank_admin/")
    else:
        return redirect("/bank_admin/")


def EditBloodInfoView(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            if request.method == "POST":
                data = request.POST
                blood = data.get("blood_group_name")
                quantity = data.get("quantity")

                try:
                    if Bloodstock.objects.filter(blood_type=blood).exists():
                        stock = Bloodstock.objects.get(blood_type=blood)

                        if blood:
                            stock.blood_type = blood
                            stock.save()
                        else:
                            pass

                        if quantity:
                            stock.quantity = quantity
                            stock.save()
                        else:
                            pass

                    else:
                        return HttpResponse("blood group not exist!")

                    stock = Bloodstock.objects.all()
                    return render(
                        request, "dashboard/blood_stock.html", context={"blood": stock}
                    )
                except Exception as e:
                    print(e)
                    return HttpResponse("error occured!")

            else:
                return HttpResponse("bad request")
        else:
            return redirect("/bank_admin/")
    else:
        return redirect("/bank_admin/")


def DeleteBloodGroupView(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            data = request.POST
            blood_group_id = data.get("bloodid")
            blood_group_id = int(blood_group_id)

            if Bloodstock.objects.filter(id=blood_group_id).exists():
                try:
                    stock = Bloodstock.objects.get(id=blood_group_id)
                    stock.delete()
                except Exception as e:
                    print(e)
                    return HttpResponse("error occured!")
            else:
                return HttpResponse("blood group ID not exist!")
            stock = Bloodstock.objects.all()
            return render(
                request, "dashboard/blood_stock.html", context={"blood": stock}
            )
        else:
            return redirect("/bank_admin/")
    else:
        return redirect("/bank_admin/")
    


def RicipientBloodReqView(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            order = Order.objects.all()
            return render(request,"dashboard/allorders.html",context={"order":order})
        else:
            return redirect("/bank_admin/")
    else:
        return redirect("/bank_admin/")
    
def OrderDetailView(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            if request.method == 'POST':
                order_id = request.POST.get("orderid")
                try:
                    order = Order.objects.get(id=order_id)
                    return render(request, "dashboard/order_detail.html", context={"order": order})
                except Order.DoesNotExist:
                    return HttpResponse("Order ID does not exist!")
            else:
                return HttpResponse("Invalid request method!")
        else:
            return redirect("/bank_admin/")
    else:
        return redirect("/bank_admin/")
    
def ConfirmOrderView(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            if request.method == 'POST':
                confirm_delivery_date = request.POST.get('confirmDeliveryDate')
                confirm_delivery_time = request.POST.get('confirmDeliveryTime')
                confirm_delivery_address = request.POST.get('confirmDeliveryAddress')
                important_message = request.POST.get('importantMessage')
                orderid = request.POST.get("orderid")
                userid = request.POST.get("userid")

                # print(request.POST)

                # if confirm_delivery_date < order_obj.delivery_date or \
                #         (confirm_delivery_time < order_obj.delivery_time):
                #     return HttpResponse("Invalid delivery date or time. Please choose a valid date and time.")

                try:
                    order_obj = Order.objects.get(id=orderid)
                    user_obj = User.objects.get(id=userid)

                    offline_delivery = Offlinedelivery(
                    delivery_date=confirm_delivery_date,
                    delivery_time=confirm_delivery_time,
                    delivery_address=confirm_delivery_address,
                    message=important_message,
                    orderid=order_obj,
                    userid=user_obj
                    )
                    offline_delivery.save()

                    try:
                        stock = Bloodstock.objects.get(blood_type=order_obj.bloodgroup)
                        stock.quantity = stock.quantity - order_obj.quantity
                        stock.save()
                    except Exception as e:
                        print(e)
                        return HttpResponse("error occured!")

                    try:
                        order_obj = Order.objects.get(id=orderid)
                        order_obj.status = True
                        order_obj.save()
                    except Exception as e:
                        print(e)
                        return HttpResponse("error occured!")     

                    return redirect("/bank_admin/ricipientsblood/")
                except Exception as e:
                    print(e)
                    return HttpResponse("error occured!")    
                
                return HttpResponse("got it")

            else:
                return HttpResponse("Invalid request method!")
        else:
            return redirect("/bank_admin/")
    else:
        return redirect("/bank_admin/")    
    

def CancelOrder(request):
    if request.method == "POST":
        data = request.POST
        id = data.get("orderid")
        
        if Order.objects.filter(id=id).exists():
            try:
                order = Order.objects.get(id=id)
                order.status = False
                order.save()

                order_obj = Order.objects.get(id=id)
                stock = Bloodstock.objects.get(blood_type=order_obj.bloodgroup)
                stock.quantity = stock.quantity - order_obj.quantity
                stock.save()
                
                return redirect("/bank_admin/")    
            except Exception as e:
                print(e)
                return HttpResponse("error occured!")  
        else:
            return HttpResponse("order id not exist!")

        # return HttpResponse("order canceled!")
    else:
        return HttpResponse("error occured! bad request!")