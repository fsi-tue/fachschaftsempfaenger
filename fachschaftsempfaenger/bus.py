"""
bus.py
------

``bus.py`` contains the functionality to show upcoming
departures of buses.

"""

import requests
from lxml import html


def get_departures(stop: str):
    """
    Get the next departures from a certain bus stop.

    - **parameters**, **types**, **return** and **return types**::
        :param stop: the busstop id of swtue
        :type stop: int
        :return: each departure consists of the time till the bus
                           departs, the bus route and the destination of the bus.
        :rtype: list of tuple
    """

    url = 'https://www.tuebus.de/vdfi-server/?stop={}'.format(stop)

    page = requests.get(url, stream=True)
    page.encoding = 'utf-8'

    # Read the second line containing the information
    for i, t in enumerate(page.iter_lines(decode_unicode=True, delimiter='\n')):
        if i == 1:
            page = t
            break

    tree = html.fromstring(page)

    lines = []
    destinations = []
    times = []

    header, *connections = zip(tree.find_class("line"),
                               tree.find_class("destination"),
                               tree.find_class("abfahrt"))

    for line, destination, time in connections:
        times.append(time.text_content().strip())
        lines.append(line.text_content().strip())
        line_destination = destination.text_content().strip()
        destinations.append(line_destination)

    return list(zip(times, lines, destinations))
