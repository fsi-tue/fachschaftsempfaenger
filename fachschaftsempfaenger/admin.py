from django.contrib import admin

# Register your models here.
from .models import Menu, Food

"""
registers the models concerning the food truck to the Django admin.
"""
admin.site.register(Food)
admin.site.register(Menu)
