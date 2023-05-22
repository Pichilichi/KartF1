from django.urls import path
from . import views


urlpatterns = [
    path('',views.getRoutes),
    path('karts/',views.getKarts),
    path('karts/<str:pk>/',views.getKart),
]