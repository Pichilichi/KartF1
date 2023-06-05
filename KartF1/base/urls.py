from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('booking/<str:pk>/', views.booking, name="booking"),

    path('create-booking/', views.createBooking, name="create-booking"),
    path('update-booking/<str:pk>/', views.updateBooking, name="update-booking"),
    path('delete-booking/<str:pk>/', views.deleteBooking, name="delete-booking"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
]
