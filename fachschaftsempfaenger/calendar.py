"""
calendar.py
-----------

``calendar.py`` contains the functionality to show upcomming
events of the student union of Computer Science in Tuebingen.
"""

from icalendar import Calendar
import pytz
import ssl
import base64
from datetime import datetime
import requests


def url(internal=False):
    if internal:
        return 'http://www.fsi.uni-tuebingen.de/'
    else:
        return 'http://www.fsi.uni-tuebingen.de/'


# returns list with events
def get_calendar_events(url=None):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    if url is None:
        url = "https://calendar.google.com/calendar/ical/suiv7mderc3amihoh1716b2avk%40group.calendar.google.com/private-85d6362dfc88ee1c8cece546aa475440/basic.ics"
    response = requests.get(url, verify=False)
    response.encoding = 'utf-8'
    calendar = Calendar.from_ical(response.text).walk('vevent')
    return calendar


def get_internal_calendare_vents():
    cal_url = 'localhost:8088/fachschaft/termine/intern/intern/ics_view'
    # use username and password
    username = 'fachschaftsnutzer'
    password = 'sparka'
    # Get calendar file and parse it to useful data
    internal_calendar = Calendar \
        .from_ical(get_remote_url(url=cal_url,
                                  auth_string=username + ':' + password)) \
        .walk('vevent')
    return internal_calendar


def get_remote_url(url=None, auth_string=None):
    '''Retrieves an URL, perhaps needing authentication'''
    # auth_string is of the form 'username:password'

    if url:
        url = str("http://") + url  # + urllib.quote(url[7:])
    if auth_string:
        base64string = base64.encodestring(auth_string)[:-1]
        response = requests.get(url, headers={
            "Authorization": "Basic %s" % base64string
        }, timeout=120)
        response.encoding = 'utf-8'
        return response.text
    else:
        return None


def get_first_n_items(n, internal=False):
    if internal:
        calendar = get_internal_calendare_vents()
    else:
        calendar = get_calendar_events()
    lines = []
    timezone = pytz.timezone('Europe/Berlin')
    actual_time = get_item_date(get_actual_utc_time())
    events = []
    for event in calendar:
        date_start = get_item_date(event['dtstart'].to_ical().decode("utf-8"))
        if date_start >= actual_time:
            events.append(event)
    events = sorted(events,
                    key=lambda event: get_item_date(event['dtstart'].to_ical().decode("utf-8")))
    for event in events:
        item_start = parse_ical_timestring(event['dtstart'].to_ical().decode("utf-8"))
        item_start = item_start.replace(tzinfo=pytz.UTC)
        item_start = item_start.astimezone(timezone)
        lines.append(item_start.strftime('%d.%m. %H:%M') + " "
                     + get_item_title(event))
    while len(lines) < n:
        lines.append("")
    return lines[:n]


def get_item_start(event):
    event = event['dtstart'].to_ical().decode("utf-8")
    return event[6:8] + '.' + event[4:6] + '.' + event[2:4] + ', ' + event[9:11] + ':' + event[11:13]


def get_item_date(ical_str):
    return ical_str[:8]


def parse_ical_timestring(ical_time_string=None):
    if ical_time_string is None:
        return
    return datetime.strptime(ical_time_string, '%Y%m%dT%H%M%SZ')


def get_item_title(event):
    return event['summary'].to_ical().decode("utf-8")


def get_actual_utc_time():
    utc_datetime = datetime.utcnow()
    return utc_datetime.strftime("%Y%m%dT%H%M%SZ")
