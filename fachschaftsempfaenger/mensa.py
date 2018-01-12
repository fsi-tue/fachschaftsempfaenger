"""
mensa.py
--------

``mensa.py`` contains the functionality to get the current menues from the
website of student services in Tuebingen.

"""
import logging

import requests
import xml.dom.minidom as minidom
import re
import datetime
from stuweparser import crawler, parser


def load_data(url):
    """
    Get the next departures from a certain bus stop.

    - **parameters**, **types**, **return** and **return types**::
        :param url: url to the website of the mensa which should be shown.
        :type url: str
        :return: the date which is loaded and a list of the meals or an
                 information that the mensa is closed on this day.
        :rtype: tuple of str and list of str
    """
    try:
        html = crawler.crawl(url)
        menue_table = parser.parse_menues(html)

        meals = [(food, student_price) for name, food, student_price, guest_price
                 in menue_table
                 if food is not None]

        day = parser.parse_current_day(html)
        date = parser.parse_current_date(html)

        date_string = day + ", " + date
        if not meals:
            meals = ["Die Mensa hat heute leider geschlossen",]

        return date_string, meals

    except BaseException as e:
        logger = logging.getLogger(__name__)
        logger.info('Error retrieving the Mensa plan: {0}'.format(str(e)))
        return []
