from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^tiles/calendar\.html$', views.calendar_tile),
    re_path(r'^tiles/sitzung\.html$', views.sitzung_tile),
    re_path(r'^tiles/bus\.html$', views.bus_tile),
    re_path(r'^tiles/forecast\.html$', views.forecast_tile),
    re_path(r'^tiles/weather\.html$', views.weather_tile),
    re_path(r'^tiles/mensa/(?P<mensa_name>\w+)\.html$', views.mensa_tile),
    re_path(r'^tiles/foodtruck\.html$', views.foodtruck_tile),
    re_path(r'^tiles/advertisement\.html$', views.advertisement_tile),
    re_path(r'^tiles/fachschaft\.html$', views.fachschaft_tile),
    re_path(r'^tiles/mastodon\.html$', views.mastodon_tile),
    path('', views.index),
]
