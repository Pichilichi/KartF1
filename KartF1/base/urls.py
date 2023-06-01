from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),

    path('booking/<str:pk>/', views.booking, name="booking"),

    path('create-booking/', views.createBooking, name="create-booking"),
    path('update-booking/<str:pk>/', views.updateBooking, name="update-booking"),
    path('delete-booking/<str:pk>/', views.deleteBooking, name="delete-booking"),
]