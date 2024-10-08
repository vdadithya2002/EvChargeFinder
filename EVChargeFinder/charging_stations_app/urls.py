from django.urls import path
from .import views

urlpatterns = [
    path('', views.station_list, name='station_list'),
    path('add/', views.add_station, name='add_station'),
    path('update/<int:station_id>/', views.update_station, name='update_station'),
    path('delete/<int:station_id>/', views.delete_station, name='delete_station'),
]
