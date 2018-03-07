"""
calendar.py
-----------

``calendar.py`` contains the functionality to show upcoming
events of the student union of Computer Science in Tuebingen.
"""
from icalendar import Calendar
import requests


def events(url):
    """
    Yields a generator of the events in the ical file provided by the url

    - **parameters**, **types**, **return** and **return types**::
        :param url: url to a ical file
        :type url: str
        :return: generator of qua­d­ru­pel in the
                 format (date, time, title, location)
        :rtype: generator
    """
    try:
        response = requests.get(url, verify=False)
        response.encoding = 'utf-8'
        calendar = Calendar.from_ical(response.text).walk('vevent')

        def _key(event):
            return event.decoded('dtstart').strftime("%d.%m.%Y %H:%M")

        calendar = sorted(calendar, key=_key, reverse=False)

    except requests.exceptions.RequestException as e:
        calendar = []
        print("Connection to caldav server failed with error: ", e)

    def _get_date(event):
        return event.decoded('dtstart').strftime("%d.%m.%Y")

    def _get_time(event):
        return event.decoded('dtstart').strftime("%H:%M")

    def _get_title(event):
        return event['summary']

    def _get_location(event):
        try:
            location = event['location']
        except KeyError as _:
            location = "TBA"
        return location

    for event in calendar:
        yield (_get_date(event), _get_time(event),
               _get_title(event), _get_location(event))
