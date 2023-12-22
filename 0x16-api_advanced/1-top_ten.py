#!/usr/bin/python3
"""Function to print top posts on a given Reddit subreddit."""
import requests
import sys
import base64


def top_ten(subreddit):
    """Prints the titles of the 10 hottest posts"""
    client_id = 'beIUiJlOBKOUF_WAKMba8A'
    client_secret = '9huuf_Qz3J00w9IiScHyBd2wFY-7fg'
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    auth = 'Basic {}'.format(
        base64.b64encode('{}:{}'.format(client_id, client_secret).encode()
                         ).decode()
    )
    headers = {
            'User-Agent': 'An alx api advanced  project/1.0',
            'Authorization': auth
        }
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
