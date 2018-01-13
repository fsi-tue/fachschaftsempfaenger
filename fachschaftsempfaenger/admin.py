from django.contrib import admin

# Register your models here.
from .models import Menu, Food

"""
registers the models concerning the food truck to the Django admin.
"""


class FoodAdmin(admin.ModelAdmin):
    search_fields = ['meal']


admin.site.register(Food, FoodAdmin)
admin.site.register(Menu)
