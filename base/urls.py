"""

"""

from django.contrib import admin
from django.urls import path, include


from home.urls import *
from donor.urls import *
from bloodbank.urls import *
from ricipient.urls import *
from hospital.urls import *

urlpatterns = [
    path("", include("home.urls")),
    path("bank_admin/",include("bloodbank.urls")),
    path("donor/", include("donor.urls")),
    path("ricipient/",include("ricipient.urls")),
    path("hospital/",include("hospital.urls")),
    path("admin/", admin.site.urls),
]
