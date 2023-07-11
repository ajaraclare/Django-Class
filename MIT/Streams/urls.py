
from django.urls import path

from.import views

urlpatterns = [
  path('', views.index, name="index"),
  path('blue/', views.blue, name="blue"),
  path('about/', views.about, name="about"),
  path('contact/', views.contact, name="contact")
]
