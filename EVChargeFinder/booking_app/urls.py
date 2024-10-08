from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_booking, name='add_booking'),
    path('', views.booking_list, name='booking_list'),
]
