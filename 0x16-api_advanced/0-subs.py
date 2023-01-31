#!/usr/bin/python3
"""Function queries Reddit API and returns
the number of subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Function returns number of subscribers"""
    URL = "https://api.reddit.com"
    headers = {
            "User-Agent": "ChangeMeClient/0.1 by Olamide"
            }
    req = requests.get("{}/r/{}/about".format(URL, subreddit),
                       headers=headers)

    if req.status_code == 404:
        return 0
    return req.json().get('data').get('subscribers')

