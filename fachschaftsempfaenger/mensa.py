"""
mensa.py
--------

``mensa.py`` contains the functionality to get the current menues from the
website of student services in Tuebingen.

"""
import json
import requests
import datetime


def load_data(url: str, mensa_id: str):
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

    # Prepare date
    today = datetime.date.today().strftime("%Y-%m-%d")
    today_string = 'Heute ' + datetime.date.today().strftime("%d.%m.%Y")
    if datetime.datetime.now().hour > 15:
        today = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        today_string = 'Morgen ' + (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")

    # Fetch the mensa data
    request = requests.get(url)
    decoded_data = request.text.encode().decode('utf-8-sig')
    data = json.loads(decoded_data)

    # If the data is empty or it's not a dictionary, return an empty list
    if data is None or (data is not None and not isinstance(data, dict)):
        return today_string, []

    # Process the mensa data
    data = data.get(mensa_id)
    meals = [(", ".join(menu["menu"]), menu["studentPrice"] + " €")
             for menu in data["menus"] if menu["menuDate"] == today]

    return today_string, meals
