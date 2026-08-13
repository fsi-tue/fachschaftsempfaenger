"""
bus.py
------

``bus.py`` contains the functionality to show upcoming
departures of buses.

"""

import json
from dataclasses import dataclass

import requests

class SSEDecodeError(Exception):
    """Raised when parsing the SSE response fails."""

@dataclass
class Departure:
    cancelled: bool
    countdown_minutes: str
    departure_time: str
    destination: str
    is_realtime: bool
    line: str
    platform: str

    def time_format(self):
        if not self.countdown_minutes.isnumeric():
            return "-"
        h = int(self.countdown_minutes) // 60
        m = int(self.countdown_minutes) % 60
        return f"{h} h {m} Min" if h > 0 else f"{m} Min"



def build_url(stop_id, departures=5, timespan=240):
    url_template = "https://dfi.swtue.de/departure_board?max_departures={}&timespan_minutes={}&stop_id={}"
    return url_template.format(departures, timespan, stop_id)

def get_departures(stop_id: str = "de:08416:10252:0:4", departures=5, timespan=240):
    """
    Get the next departures from a certain bus stop.

    - **parameters**, **types**, **return** and **return types**::
        :param stop_id: the busstop id of swtue
        :type stop_id: int
        :return: each departure consists of the time till the bus departs, the bus route and the destination of the bus among other data.
        :rtype: list of Departure
    """

    url = build_url(stop_id, departures, timespan)

    try:
        stream = requests.get(url, stream=True)
        stream.encoding = 'utf-8'
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch departures: {e}") from e

    lines = stream.iter_lines(decode_unicode=True, delimiter="\n")
    data = None
    for l in lines:
        if l == "event: departures":
            data = next(lines)
            break
    stream.close()

    if data is None:
        raise SSEDecodeError("No departures event found in SSE response")

    if data[:6] != "data: ":
        raise SSEDecodeError(f"Unexpected data format: {data!r}")    
    
    try:
        data = json.loads(data[6:])
    except json.JSONDecodeError as exc:
        raise SSEDecodeError("Invalid JSON in departures event") from exc

    return [Departure(
        dep.get("cancelled"), 
        dep.get("countdown_minutes"), 
        dep.get("departure_time"), 
        dep.get("destination"), 
        dep.get("is_realtime"), 
        dep.get("line"), 
        dep.get("platform")
    ) for dep in data]
