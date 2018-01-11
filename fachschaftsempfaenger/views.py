import datetime
import json

from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.template import loader

import requests

from . import calendar
from . import weather
from . import mensa
from . import bus


def sitzung_tile(request):
    return render(request, 'tiles/sitzung.html')


def calendar_tile(request):
    return render(request, 'tiles/calendar.html')


def bus_tile(request):
    events = bus.get_departures('Sand Drosselweg')

    return render(request, 'tiles/bus.html', dict(events=events))


def forecast_tile(request):
    import urllib.request
    response = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=Tuebingen,DE&appid=806b3582a0c4787e47e950a6274b681a&units=metric')
    content = response.read()
    data = json.loads(content.decode('utf-8'))
    #

    today_string = datetime.datetime.now().strftime('%Y-%m-%d')
    tomorrow_string = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    days = dict()
    for d in data['list']:
        tmp_day = d['dt_txt'][:10]
        if not (tmp_day == today_string or tmp_day == tomorrow_string):
            continue
        if ' 09:00' in d['dt_txt'] or ' 12:00' in d['dt_txt'] or '18:00' in d['dt_txt']:
            if tmp_day in days:
                days[tmp_day].append(d)
            else:
                days[tmp_day] = [d]
    if today_string in days:
        days_array = [days[today_string], days[tomorrow_string]]
    else:
        days_array = [days[tomorrow_string]]

    return render(request, 'tiles/forecast.html', dict(data=days, data_array=days_array))


def weather_tile(request, use_kelvin=False):
    ctx = weather.weather_data()
    ctx['link'] = 'https://wetteronline.de/wetter-aktuell/tuebingen'
    return render(request, 'tiles/weather.html', ctx)


def mensa_tile(request):
    mensa_website = "http://www.my-stuwe.de/mensa/mensa-morgenstelle-tuebingen"
    date_string, meals = mensa.load_data(mensa_website)

    context = dict(meals=meals,
                   link=mensa_website, date=date_string)

    return render(request, 'tiles/mensa.html', context)


def index(request):
    return render(request, 'index.html')
