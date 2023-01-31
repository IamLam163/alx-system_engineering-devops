#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """recursive function that returns a list"""
    URL = "https://api.reddit.com"
    headers = {"User-Agent": "ChangeMeClient/0.1 by Olamide"}
    params = {
        "after": after,
        "count": count
    }
    req = requests.get("{}/r/{}/hot".format(URL, subreddit),
                       headers=headers, params=params)
    if req.status_code == 404:
        return None
    data = req.json().get('data')
    after = data.get('after')
    count += data.get('dist')
    if after is not None:
        recurse(subreddit, hot_list, after, count)
    children = data.get('children')
    for child in children:
        hot_list.append(child.get('data').get('title'))

    return hot_list
