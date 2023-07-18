
from django.urls import path,include

from . import views

app_name ="class"

urlpatterns = [
    path('',views.home , name="home"),
    path('contact/',views.contact,name="Contact"),
    path('about/', include("Streams.urls")),
    path('services/',views.services, name="services")
]