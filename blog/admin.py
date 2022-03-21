from django.contrib import admin
from .models import Item
from .models import Shop
from .models import Price

admin.site.register(Item)
admin.site.register(Shop)
admin.site.register(Price)