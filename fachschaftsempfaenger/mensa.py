"""
mensa.py
--------

``mensa.py`` contains the functionality to get the current menues from the
website of student services in Tuebingen.

"""
import json
import requests
import datetime


def load_data(url, mensa_id):
    """
    Get today's meals from a mensa of the student services in Tuebingen.
    The current mapping of the mensa IDs can be found under https://www.my-stuwe.de/wp-json/mealplans/v1/canteens/.

    - **parameters**, **types**, **return** and **return types**::
        :param url: url to the website of the mensa which should be shown.
        :param mensa_id: ID (the JSON key) of the mensa to be parsed.
        :type url: str
        :return: the date which is loaded and a list of the meals or an
                 information that the mensa is closed on this day.
        :rtype: tuple of str and list of str
    """

    request = requests.get(url)
    decoded_data = request.text.encode().decode('utf-8-sig')
    data = json.loads(decoded_data)[mensa_id]

    today = datetime.date.today().strftime("%Y-%m-%d")
    meals = [(", ".join(menu["menu"]), menu["studentPrice"] + " €")
             for menu in data["menus"] if menu["menuDate"] == today]

    today = datetime.date.today().strftime("%d.%m.%Y")

    return today, meals
