from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tiles/calendar\.html$', views.calendar_tile),
    url(r'^tiles/sitzung\.html$', views.sitzung_tile),
    url(r'^tiles/bus\.html$', views.bus_tile),
    url(r'^tiles/forecast\.html$', views.forecast_tile),
    url(r'^tiles/weather\.html$', views.weather_tile),
    url(r'^tiles/mensa\.html$', views.mensa_tile),
    url(r'^tiles/foodtruck\.html$', views.foodtruck_tile),
    url(r'^$', views.index),
]
