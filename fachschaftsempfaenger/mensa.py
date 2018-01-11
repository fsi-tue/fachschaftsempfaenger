import logging

import requests
import xml.dom.minidom as minidom
import re
import datetime
from stuweparser import crawler, parser


def load_data(url):
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
