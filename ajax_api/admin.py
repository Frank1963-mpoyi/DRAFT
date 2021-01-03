from django.contrib import admin
from .models import Shirt


class ShirtAdmin(admin.ModelAdmin):
    list_display = ('brand', 'price', 'visited')


admin.site.register(Shirt, ShirtAdmin)
