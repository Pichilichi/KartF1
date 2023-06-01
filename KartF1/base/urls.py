from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('booking/<str:pk>/', views.booking, name="booking"),

    path('create-booking/', views.createBooking, name="create-booking"),
    path('update-booking/<str:pk>/', views.updateBooking, name="update-booking"),
]