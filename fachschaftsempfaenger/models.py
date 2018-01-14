from django.db import models
from django.utils import timezone


class Food(models.Model):
    """
    `Food` defines an item for sale at the food truck. Each item has a name, a price and a field that specifies
    wether it's vegan or not. An item can appear on several menus (see below).
    """
    meal = models.TextField(verbose_name="Name", editable=True, blank=False)
    price = models.DecimalField(verbose_name="Preis in €", max_digits=4, decimal_places=2)
    vegan = models.BooleanField(verbose_name="vegan", default=False)

    def __str__(self):
        return self.meal

    class Meta:
        verbose_name = "Essen"
        verbose_name_plural = "Essen"


class Menu(models.Model):
    """
    `Menu` represents the menu at the food truck for a specific day. Each menu must have a date and can list several
    food items (many-to-many-relationship with Food: a food item can appear on many menus,
    a menu has got many items)
    """
    date = models.DateField(verbose_name="Datum", editable=True, blank=False, default=timezone.now)
    items = models.ManyToManyField(Food, related_name="menu_item")

    class Meta:
        verbose_name = "Speisekarte"
        verbose_name_plural = "Speisekarten"

    def __str__(self):
        return "Speisekarte für " + str(self.date.strftime("%d.%m.%Y"))

