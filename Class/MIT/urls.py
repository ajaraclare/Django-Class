
from django.urls import path

from . import views

urlpatterns = [
    path('',views.practise, name="practise"),
    path('contact/', views.contact, name="contact")
]