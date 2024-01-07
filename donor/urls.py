from django.urls import path
from .views import *

urlpatterns = [
    path("",RegisterView),
    path("d_login/",LoginView,name="d_login"),
    path("d_dashboard/",DashboardView,name="d_dashboard"),
    path("d_info/",InfoView,name="d_info"),
    path("d_logout/",LogoutView,name="d_logout"),
]