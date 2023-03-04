from django.contrib import admin

from .models import OwnerRent, Sell_flat, Sell_land

# Register your models here.

admin.site.register(Sell_flat)
admin.site.register(Sell_land)
admin.site.register(OwnerRent)
