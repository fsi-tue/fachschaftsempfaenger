"""
mensa.py
--------

``mensa.py`` contains the functionality to get the current menues from the
website of student services in Tuebingen.

"""
from urllib.request import Request, urlopen
import json
import datetime


def load_data(url):
    """
    Get today's meals from a mensa of the student services in Tuebingen.

    - **parameters**, **types**, **return** and **return types**::
        :param url: url to the website of the mensa which should be shown.
        :type url: str
        :return: the date which is loaded and a list of the meals or an
                 information that the mensa is closed on this day.
        :rtype: tuple of str and list of str
    """
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/5'

                                     '37.11 (KHTML, like Gecko) '
                                     'Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,'
                         'application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}

    request = Request(url, headers=headers)
    response = urlopen(request)

    data = json.load(response)["631"]

    today = datetime.date.today().strftime("%Y-%m-%d")
    meals = [(", ".join(menu["menu"]), menu["studentPrice"])
             for menu in data["menus"] if menu["menuDate"] == today]

    today = datetime.date.today().strftime("%d.%m.%Y")


    return today, meals
