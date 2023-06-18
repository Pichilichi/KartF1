from django.contrib import admin

from .models import Kart, Circuit, Category, Booking, Equipment, Message, Order, OrderItem, ShippingAdress

admin.site.register(Kart)
admin.site.register(Circuit)
admin.site.register(Category)
admin.site.register(Booking)
admin.site.register(Equipment)
admin.site.register(Message)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAdress)