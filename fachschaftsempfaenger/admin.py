from django.contrib import admin

from .models import Menu, Food


class FoodAdmin(admin.ModelAdmin):
    search_fields = ['meal']


admin.site.register(Food, FoodAdmin)
admin.site.register(Menu)
