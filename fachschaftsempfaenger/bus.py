"""
bus.py
------

``bus.py`` contains the functionality to show upcomming
departures of buses.

"""

import requests
from lxml import html
from datetime import datetime, timedelta


def get_departures(stop):
    """
    Get the next departures from a certain bus stop.

    - **parameters**, **types**, **return** and **return types**::
        :param stop: the busstop id of swtue
        :type stop: int
        :return: each departure consist of the time till the bus
                           departs, the busline and the destination of the bus.
        :rtype: list of tuple
    """
    stations = {
        'Sand Drosselweg': 25207

    }

    url = ('https://www.swtue.de/abfahrt.html?halt='
           '%d' % stations[stop])

    page = requests.get(url)
    tree = html.fromstring(page.content)

    lines = []
    destinations = []
    times = []

    header, *connections = zip(tree.find_class("linie"),
                              tree.find_class("richtung"),
                              tree.find_class("abfahrt"))

    for line, destination, time in connections:
        times.append(time.text_content().strip())
        lines.append(line.text_content().strip())
        line_destination = destination.text_content().strip()
        destinations.append(line_destination.encode('utf-8', 'ignore'))

    return list(zip(times, lines, destinations))
