from django.contrib import admin

from .models import Kart, Circuit, Category, Booking, Equipment

admin.site.register(Kart)
admin.site.register(Circuit)
admin.site.register(Category)
admin.site.register(Booking)
admin.site.register(Equipment)