from django.urls import path
from .views import *

urlpatterns = [
    path("",LoginView),
    path("dashboard/",DashboardView,name="bank_dashboard"),
    
    path("donor_requets/",DonorRequestView,name="donor_new_requests"),
    path("approve_donor_acc",DonorAccountReview,name="approve_donor"),

    path("ricipient_requets/",RicipientRequestView,name="ricipient_new_requests"),
    path("approve_ricipient_acc",RicipientAccountReview,name="approve_ricipient"),

    path("hospital_requets/",HospitalRequestView,name="hospital_new_requests"),
    path("hospital_ricipient_acc",HospitalAccountReview,name="approve_staff"),

    path("blood_stock",BloodStockView,name="blood_stock"),
    path("add_blood_group/",AddBloodGroupView,name="blood_group"),
    path("editbloodinfo/",EditBloodInfoView,name="editBloodInfo"),
    path("deletebloodgroup/",DeleteBloodGroupView,name="deletebloodgroup"),

    path("ricipientsblood/",RicipientBloodReqView,name="ricipients_blood_req"),
    path("orderdetail/",OrderDetailView,name="order_detail"),
    path("confirmorder/",ConfirmOrderView,name="confirm_order"),
    path("cancelorder/",CancelOrder,name="cancel_order"),
]