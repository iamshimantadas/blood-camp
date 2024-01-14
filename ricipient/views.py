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
            is_receipient=True,
        )
        try:
            user.set_password(password)
            user.save()
            context = {"register_email": email, "register_password": password, "register_phone":phone}
            return render(request, "r_login.html", context)
        except Exception as e:
            print(e)
            return HttpResponse("error occured!")
    else:
        return render(request,"r_register.html")
    
    
def LoginView(request):
    if request.method == "POST":
        data = request.POST
        phone = data.get("phone")
        phone = int(phone)
        try:
            user = User.objects.get(email=data.get("email"))
            auth = authenticate(email=data.get("email"), password=data.get("password"))
            
            if auth:
                if phone == user.phone:
                    login(request, user)
                    return redirect("/ricipient/r_dashboard/")
                else:
                    return HttpResponse("phone number not match! Please enter correct one!")
            else:
                return HttpResponse("please enter right credentials!")
        except Exception as e:
            print(e)
            return HttpResponse("error occured!")
            
    else:
        user = request.user
        if user.is_authenticated:
            if user.is_receipient:
                acc_status = user.status
                context = {"status": acc_status}
                return render(request, "dashboard/r_dashboard.html", context)
            else:
                return render(request, "r_login.html")
        else:
            return render(request, "r_login.html")
        


def DashboardView(request):
    user = request.user
    if user.is_authenticated:
        if user.is_receipient:
            acc_status = user.status
            context = {"status": acc_status}
            return render(request, "dashboard/r_dashboard.html", context)
        else:
            return HttpResponse("you are not ricipient! bad request!")
    else:
        return redirect("/ricipient/r_login/")


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

        return redirect("/ricipient/r_login/")
    else:
        user = request.user
        if user.is_authenticated:
            if user.is_receipient:
                user_obj = User.objects.get(email=user.email)
                print(user_obj)
                context = {"data": user_obj}
                return render(request, "dashboard/r_info.html", context)
            else:
                return HttpResponse("bad request!")
        else:
            return redirect("/ricipient/r_login/")


def LogoutView(request):
    if request.user.is_authenticated:
        if request.user.is_receipient:
            logout(request)
            return redirect("/")
        else:
            return HttpResponse("bad request!")
    else:
        return redirect("/ricipient/r_login/")
    

def AddNewBloodRequestView(request):
    if request.method == "POST":
        data = request.POST
        
        if request.user.is_receipient:
            if request.user.status:
                blood = data.get('blood_group')
                try:
                    stock = Bloodstock.objects.get(id=blood)
                    quan = data.get('quantity')
                    quan = int(quan)
                    quan2 = int(stock.quantity)
                    # print(quan)
                    # print(quan2)

                    if not quan < quan2:
                        try:
                            bloodgrpid = Bloodstock.objects.get(id=blood)
                            order = Order(
                                userid = User.objects.get(id=request.user.id),
                                name=data.get('full_name'),
                                email=data.get('email'),
                                age=data.get('age'),
                                bloodgroup=bloodgrpid,  # Assuming 'blood_group' is the ID of the selected blood group
                                quantity=data.get('quantity'),
                                address=data.get('address'),
                                idproff=data.get('government_id'),
                                idtype=data.get('profession_type'),
                                contactno=data.get('contact_number'),
                                emer_contactno=data.get('emergency_contact'),
                                deliverdate=data.get('delivery_date'),
                                delivertime=data.get('delivery_time'),
                                deliverymode=data.get('delivery_mode'),
                                status=False,
                            )
                            order.save()
                            # return redirect("/ricipient/r_trackallreq/")
                            return HttpResponse(''' 
                            Current This Blood Group Out Of Stock From Us.But We have registered your request to us.
                                                We will inform you if stock will available! <a href='/ricipient/r_login/'>click here</a>
                            ''')
                        except Exception as e:
                            print(e)
                            return HttpResponse("error occured!")
                    else:
                        try:
                            bloodgrpid = Bloodstock.objects.get(id=blood)
                            order = Order(
                                userid = User.objects.get(id=request.user.id),
                                name=data.get('full_name'),
                                email=data.get('email'),
                                age=data.get('age'),
                                bloodgroup=bloodgrpid,  # Assuming 'blood_group' is the ID of the selected blood group
                                quantity=data.get('quantity'),
                                address=data.get('address'),
                                idproff=data.get('government_id'),
                                idtype=data.get('profession_type'),
                                contactno=data.get('contact_number'),
                                emer_contactno=data.get('emergency_contact'),
                                deliverdate=data.get('delivery_date'),
                                delivertime=data.get('delivery_time'),
                                deliverymode=data.get('delivery_mode'),
                                status=False,
                            )
                            order.save()
                            return redirect("/ricipient/r_trackallreq/")
                        except Exception as e:
                            print(e)
                            return HttpResponse("error occured!")
                    
                except Exception as e:
                    print(e)
                    return HttpResponse("error occured!")
            else:
                return HttpResponse("Your account is not active!")
        else:
            return HttpResponse("bad request")

    else:
        stock = Bloodstock.objects.all()    
        return render(request,"dashboard/r_new_blood_request.html",context={"blood":stock})


def TrackAllRequestView(request):
    if request.user.is_authenticated:
        if request.user.is_receipient:
            if request.user.status:
                user = request.user
                try:
                    user_obj = User.objects.get(id=user.id)
                    order = Order.objects.filter(userid=user_obj)
                    return render(request,"dashboard/r_orders.html",context={"order":order})
                except Exception as e:
                    print(e)
                    return HttpResponse("error occured!")
            else:
                return HttpResponse("Your account is not approved! Please wait for confirmation!")
        else:
            return HttpResponse("bad request!")
    else:
        return redirect("/ricipient/r_login/")
    
def OfflineDeliveryTrack(request):
    # if request.user.is_authenticated:
    #     if request.user.is_receipient:
    #         if request.user.status:
    #             if request.method  == "POST":
    #                 data = request.POST
    #                 orderid = data.get("orderid")
    #                 try:
    #                     order_obj = Order.objects.filter(id=orderid).last()
    #                     print(order_obj)
    #                     if order_obj.status:
    #                         delivery = Offlinedelivery.objects.get(orderid=order_obj)
    #                         print(delivery)
    #                         return render(request,"dashboard/r_delivery_detail.html",context={"delivery":delivery})
    #                     else:
    #                         return HttpResponse("order not confirmed by admin!")
    #                 except Exception as e:
    #                     print(e)
    #                     return HttpResponse("error occured")
                        
    #             else:
    #                 return HttpResponse("bad request")
    #         else:
    #             return HttpResponse("Your account is not approved! Please wait for confirmation!")
    #     else:
    #         return HttpResponse("bad request!")
    # else:
    #     return redirect("/ricipient/r_login/")

    if request.user.is_authenticated:
        if request.user.is_receipient:
            if request.user.status:
                if request.method == "POST":
                    data = request.POST
                    orderid = data.get("orderid")
                    try:
                        order_obj = Order.objects.filter(id=orderid).last()
                        print(order_obj)
                        if order_obj.status:
                            # Use filter instead of get to handle multiple objects
                            deliveries = Offlinedelivery.objects.filter(orderid=order_obj)
                            print(deliveries)

                            if deliveries.exists():
                                # Choose the delivery you want to display
                                delivery = deliveries.last()
                                return render(request, "dashboard/r_delivery_detail.html", context={"delivery": delivery})
                            else:
                                return HttpResponse("No delivery found for the given order!")
                        else:
                            return HttpResponse("Order not confirmed by admin!")
                    except Exception as e:
                        print(e)
                        return HttpResponse("Error occurred")
                else:
                    return HttpResponse("Bad request")
            else:
                return HttpResponse("Your account is not approved! Please wait for confirmation!")
        else:
            return HttpResponse("Bad request!")
    else:
        return redirect("/ricipient/r_login/")    