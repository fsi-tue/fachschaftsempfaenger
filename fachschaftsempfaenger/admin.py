from django.contrib import admin

from .models import Menu, Food, Advertisement, Fachschaft


class FoodAdmin(admin.ModelAdmin):
    search_fields = ['meal']
    list_display = ['meal', 'price']


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_date', 'end_date', 'image']


class FachschaftAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    ordering = ['last_name']


admin.site.register(Food, FoodAdmin)
admin.site.register(Menu)
admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Fachschaft, FachschaftAdmin)
