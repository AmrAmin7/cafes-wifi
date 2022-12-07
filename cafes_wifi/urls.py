from django.contrib import admin
from django.urls import path

from cafes_wifi import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cafes/<int:cafe_id>/', views.city_details, name='city_details'),
]
