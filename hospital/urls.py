from django.urls import path
from .views import *

urlpatterns = [
    path("",RegisterView),
    path("login/",LoginView,name="login"),
    path("dashboard/",DashboardView,name="dashboard"),
    path("info/",InfoView,name="info"),
    path("logout/",LogoutView,name="logout"),
]