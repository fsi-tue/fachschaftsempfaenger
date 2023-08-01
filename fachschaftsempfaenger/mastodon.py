"""
mastodon.py
--------

``mastodon.py`` contains the functionality to get the latest toot of the
fsi_tue mastodon account

"""
import json
import requests
import datetime


def load_data(instance, username):
    """
    Get the latest toot from a mastodon account.

    - **parameters**, **types**, **return** and **return types**::
        :param instance: url to the mastodon instance the desired profile is on
        :param username: The desired profiles username
        :type instance: str
        :type username: str
        :return: the date which is loaded and the latest toot
        :rtype: dict
    """

    url = instance + '/users/' + username + '/outbox?min_id=0&page=true'

    request = requests.get(url)
    decoded_data = request.text.encode().decode('utf-8-sig')
    data = json.loads(decoded_data)['orderedItems']

    last_toot = [ {'id':         toot['id'],
                   'content':    toot['object']['content'],
                   'attachment': toot['object']['attachment'] }
                 for toot in data
                 if toot['type'] == 'Create' and
                    not toot['object']['inReplyTo']][0]

    return last_toot['id'], last_toot['content'], last_toot['attachment']
