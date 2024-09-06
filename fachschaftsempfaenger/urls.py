from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    re_path(r'^tiles/calendar\.html$', views.calendar_tile),
    re_path(r'^tiles/sitzung\.html$', views.sitzung_tile),
    re_path(r'^tiles/bus\.html$', views.bus_tile),
    re_path(r'^tiles/forecast\.html$', views.forecast_tile),
    re_path(r'^tiles/weather\.html$', views.weather_tile),
    re_path(r'^tiles/mensa_morgenstelle\.html$', views.mensa_morgenstelle_tile),
    re_path(r'^tiles/mensa_wilhelmstraße\.html$', views.mensa_wilhelmstraße_tile),
    re_path(r'^tiles/foodtruck\.html$', views.foodtruck_tile),
    re_path(r'^tiles/advertisement\.html$', views.advertisement_tile),
    re_path(r'^tiles/fachschaft\.html$', views.fachschaft_tile),
    re_path(r'^tiles/mastodon\.html$', views.mastodon_tile),
    re_path(r'^$', views.index),
]
