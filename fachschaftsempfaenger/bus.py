"""
bus.py
------

``bus.py`` contains the functionality to show upcoming
departures of buses.

"""

import json
import time
from dataclasses import dataclass

import requests

API_URL = "https://dfi.swtue.de/departure_board"

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
        return f"{h}h {m}min" if h > 0 else f"{m}min"


def get_departures(stop_id: str = "de:08416:10252:0:4", departures=5, timespan=240):
    """
    Get the next departures from a certain bus stop.

    - **parameters**, **types**, **return** and **return types**::
        :param stop_id: the busstop id of swtue
        :type stop_id: str
        :return: each departure consists of the time till the bus departs, the bus route and the destination of the bus among other data.
        :rtype: list of Departure
    """

    params = {"max_departures": departures, "timespan_minutes": timespan, "stop_id": stop_id}

    start_time = time.monotonic()

    try:
        with requests.get(API_URL, params=params, stream=True, timeout=(5, 15)) as stream:
            stream.encoding = 'utf-8'
            lines = stream.iter_lines(decode_unicode=True, delimiter="\n")
            data = None
            for l in lines:
                if time.monotonic() - start_time > 10:
                    raise TimeoutError("Timeout: Server did not send a departures event in time.")
                prefix, _, eventtype = l.partition(":")
                if prefix.strip() == "event" and eventtype.strip() == "departures":
                    try:
                        data = next(lines)
                    except StopIteration:
                        raise SSEDecodeError("Stream got closed after event line without sending data")
                    break
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch departures: {e}") from e

    if data is None:
        raise SSEDecodeError("No departures event found in SSE response")

    prefix, _, payload = data.partition(":")
    if prefix.strip() != "data":
        raise SSEDecodeError(f"Unexpected data format: {data!r}")    
    
    try:
        data = json.loads(payload.strip())
    except json.JSONDecodeError as exc:
        raise SSEDecodeError("Invalid JSON in departures event") from exc

    return [
        Departure(
            dep.get("cancelled", False), 
            dep.get("countdown_minutes", ""), 
            dep.get("departure_time", ""), 
            dep.get("destination", ""), 
            dep.get("is_realtime", True), 
            dep.get("line", ""), 
            dep.get("platform", "")
        ) 
        for dep in data
    ]
