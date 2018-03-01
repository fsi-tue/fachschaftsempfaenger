"""
weather.py
----------

``weather.py`` contains the functionality to get current weather details.

The functions are adapted from the student union of Computer Science at the
university of Freiburg.
"""
import requests
from lxml import html


def weather_data(use_kelvin=False):
    page = requests.get('http://www.wetteronline.de/wetter-aktuell/tuebingen')
    tree = html.fromstring(page.content)

    root_elem = tree.get_element_by_id('humidity').getparent()
    data = (root_elem.
            getchildren()[0].getchildren()[1].getchildren()[2].
            getchildren()[0].text_content().split('\n'))

    temperature_string = float(data[2].rstrip('° C'))
    temperature_unit = " °C"
    temperature_format = "{:.1f}"
    if (use_kelvin):
        temperature_string += 273.1
        temperature_format = "{:.0f}"
        temperature_unit = " K"

    weather_string = data[3].lstrip()

    rel_humidity_parts = (root_elem.getchildren()[1].getchildren()[1]
                          .getchildren()[2].getchildren()[0].text_content()
                          .split('\n'))
    rel_humidity = rel_humidity_parts[2].lstrip()
    # sight = rel_humidity_parts[3].lstrip()

    rain_parts = (root_elem.getchildren()[2].getchildren()[1]
                  .getchildren()[2].getchildren()[0].text_content()
                  .split('\n'))
    rain_string = rain_parts[2].lstrip()
    rain_type = rain_parts[3].lstrip()

    wind_parts = (root_elem.getchildren()[3].getchildren()[1].getchildren()[2]
                  .getchildren()[0].text_content().split('\n'))
    wind_strength_metric = wind_parts[2].lstrip()
    # wind_strength_bft = wind_parts[3].lstrip()
    # wind_strength_max = wind_parts[4].lstrip()
    # wind_direction_degree = wind_parts[5].lstrip()
    wind_direction = wind_parts[6].lstrip()

    cloudsdata = (root_elem.getchildren()[4].getchildren()[1].getchildren()[2]
                  .getchildren()[0].getchildren()[1].text_content()
                  .lstrip().split(' '))
    clouds_string = cloudsdata[len(cloudsdata) - 1]

    pressure_parts = (root_elem.getchildren()[5].getchildren()[1]
                      .getchildren()[2].getchildren()[0].text_content()
                      .split('\n'))
    pressure = pressure_parts[2].lstrip()
    # pressure_tendance = pressure_parts[3].lstrip()

    return {
        'weather': weather_string,
        'rain': rain_string,
        'rain_type': rain_type,
        'clouds': clouds_string,
        'humidity': rel_humidity,
        'pressure': pressure,
        'temperature': temperature_format.format(temperature_string),
        'temperature_unit': temperature_unit,
        'wind_strength': wind_strength_metric,
        'wind_direction': wind_direction,
    }
