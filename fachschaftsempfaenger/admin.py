from django.contrib import admin

from .models import Menu, Food, Ad


class FoodAdmin(admin.ModelAdmin):
    search_fields = ['meal']


class AdAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_date', 'end_date', 'image']


admin.site.register(Food, FoodAdmin)
admin.site.register(Menu)
admin.site.register(Ad, AdAdmin)
