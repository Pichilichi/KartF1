from django.urls import path
from . import views


urlpatterns = [
    path('',views.getRoutes),
    path('karts/',views.getKarts),
    path('karts/create/',views.createKart),
    path('karts/<str:pk>/update',views.updateKart),
    path('karts/<str:pk>/delete',views.deleteKart),
    path('karts/<str:pk>/',views.getKart),
]