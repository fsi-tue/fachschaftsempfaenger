import datetime
import json

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.template import loader

import requests

from fachschaftsempfaenger.models import Food, Menu, Advertisement, Member
from . import calendar
from . import weather
from . import mensa
from . import bus
from . import __author__ as author
from . import __repository_url__ as repo_url


def sitzung_tile(request):
    return render(request, 'tiles/sitzung.html')


def calendar_tile(request):
    ical_url = "http://fachschaftsempfaenger.fsi.uni-tuebingen.de:5232/fsi/1928360d-1133-10b2-d238-b7335c4f778f/"

    number_events = 5

    try:
        event_generator = calendar.events(ical_url)
        events = [next(event_generator) for _ in range(number_events)]
    except:
        event_generator = calendar.events(ical_url)
        events = list(event_generator)#[:number_events]

    url = "www.fsi.uni-tuebingen.de"

    return render(request, 'tiles/calendar.html', dict(events=events, link=url))


def bus_tile(request):
    stopid = 25207
    url = 'https://www.swtue.de/abfahrt.html?halt={}'.format(stopid)
    events = bus.get_departures(stopid)

    return render(request, 'tiles/bus.html', dict(events=events, link=url))


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

    try:
        date_string, meals = mensa.load_data(mensa_website)
        context = dict(meals=meals,
                       link=mensa_website, date=date_string)
    except BaseException:
        print("Error retrieving the Mensa plan!")
        context = dict(meals=None, link=mensa_website, hidden=True)

    return render(request, 'tiles/mensa.html', context)


def foodtruck_tile(request):
    """
    Renders the tile for the food truck. It queries the models `Menu` and `Food` to aquire a menu for the current week
    (a menu that's either meant for the current day or a day that is at most 6 days into the future).
    If no menu exists for this time period, an exception is thrown and and a `None` object is passed to the template.
    """
    try:
        menu_date = Menu.objects.get(date__gte=timezone.now(),
                                     date__lte=timezone.now() + datetime.timedelta(days=6)).date.strftime("%d.%m.%Y")
        menu = Food.objects.filter(menu_item__date__gte=timezone.now(),
                                   menu_item__date__lte=timezone.now() + datetime.timedelta(days=6))

        context = dict(menu=menu, menu_date=menu_date)
    except ObjectDoesNotExist:
        print("No appropriate food truck items or menus found for the current week!")
        context = dict(menu=None, hidden=True)

    return render(request, 'tiles/foodtruck.html', context)


def advertisement_tile(request):
    """
    Renders a custom advertisement message to be displayed.
    """
    # Are there any messages to be displayed right now? If there are, select one at random.
    # Note that this query is quite expensive and could potentially slow the load time of this tile down.
    if Advertisement.objects.filter(
            start_date__lte=timezone.now(),
            end_date__gte=timezone.now()
    ):
        qs = Advertisement.objects.filter(
            start_date__lte=timezone.now(),
            end_date__gte=timezone.now()).order_by('?').first()
        context = dict(advertisement=qs)
    else:
        print("There are no advertisement messages to be displayed right now!")
        context = dict(advertisement=None, hidden=True)

    return render(request, 'tiles/advertisement.html', context)


def fachschaft_tile(request):
    """
    Randomly chooses a picture of a member of the student union
    and displays it alongside their field of study etc.
    """
    # Select one of the people in the database at random and display their details.
    # Note that this query is quite expensive and could potentially slow the load time of this tile down.
    if Member.objects.exists():
        qs = Member.objects.order_by('?').first()
        context = dict(person=qs)
    else:
        print("No people of the student union found in database!")
        context = dict(person=None, hidden=True)

    return render(request, 'tiles/fachschaft.html', context)


def index(request):
    """
    The tiles that are displayed on the main page are loaded via JQuery (see index.html file itself)
    Additional data to be displayed (i.e. footer, overlays etc.) can be passed via the context.
    """
    copy = '2018 ' + author

    context = dict(author=author, copyright=copy, repo_url=repo_url)

    return render(request, 'index.html', context)
