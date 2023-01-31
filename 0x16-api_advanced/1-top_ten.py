#!/usr/bin/python3
"""Function queried Reddit api and prints the titles
of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """returns first 10 posts"""
    URL = "https://api.reddit.com"
    headers = {"User-Agent": "ChangeMyClient/0.1 by Olamide"}
    params = {"limit": 10}

    req = requests.get("{}/r/{}".format(URL, subreddit),
                       headers=headers, params=params)
    if req.status_code == 404:
        return print(None)
    children = req.json().get('data').get('children')
    print("\n".join([child.get('data').get('title') for child in children]))
