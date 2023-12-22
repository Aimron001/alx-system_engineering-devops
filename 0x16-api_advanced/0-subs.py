#!/usr/bin/python3
"""queries the Reddit API and returns the
number of subscribers for a given subreddit"""

import requests
import base64
import sys


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of
    subscribers for a given subreddit"""

    client_id = 'beIUiJlOBKOUF_WAKMba8A'
    client_secret = '9huuf_Qz3J00w9IiScHyBd2wFY-7fg'

    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
            'User-Agent': 'An alx api advanced  project/1.0',
            'Authorization': f'Basic {base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()}'
        }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
