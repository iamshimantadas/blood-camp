from django.urls import path
from .views import *

urlpatterns = [
    path("",RegisterView),
    path("r_login/",LoginView,name="r_login"),
    path("r_dashboard/",DashboardView,name="r_dashboard"),
    path("r_info/",InfoView,name="r_info"),
    path("r_logout/",LogoutView,name="r_logout"),
    path("r_new_blood_request/",AddNewBloodRequestView,name="r_addnewbloodreq"),
    path("r_trackallreq/",TrackAllRequestView,name="r_trackallreq"),
    path("r_offlinedelivery/",OfflineDeliveryTrack,name="r_offlinedelivery"),
]