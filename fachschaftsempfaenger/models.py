from datetime import timedelta
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


class Advertisement(models.Model):
    """
    Ability to display a custom message or an image to advertise for events of the student union (i.e. 'Clubhausfest',
    'Sommerfest') or give other additional information.
    It must have a start date and an optional end date, this allows for messages to only be displayed for a certain time.
    """
    start_date = models.DateField(verbose_name="Startdatum",
                                  editable=True,
                                  blank=False,
                                  default=timezone.now)
    end_date = models.DateField(verbose_name="Enddatum",
                                editable=True,
                                blank=False,
                                default=timezone.now()+timedelta(days=7))
    image = models.ImageField(verbose_name="Grafik", blank=False)
    text = models.TextField(verbose_name="Nachricht", max_length=280, blank=True)

    class Meta:
        verbose_name = "Werbe-Nachricht"
        verbose_name_plural = "Werbe-Nachrichten"

    def __str__(self):
        return self.image.name


class Fachschaft(models.Model):
    """"
    Ability to display a member of the student union with picture, field of study,
    memberships in university committees etc.
    """

    first_name = models.TextField(verbose_name="Vorname",
                                  editable=True,
                                  blank=False,
                                  default="",
                                  )

    last_name = models.TextField(verbose_name="Nachname",
                                 editable=True,
                                 blank=False,
                                 default="",
                                 )

    image = models.ImageField(verbose_name="Foto", default='no_pic_grace.png')
    study = models.TextField(verbose_name="Studiengang", blank=False)
    committees = models.TextField(verbose_name="Gremien/andere Aktivitäten", blank=True)

    class Meta:
        verbose_name = "Fachschaftsmitglied"
        verbose_name_plural = "Fachschaftsmitglieder"
