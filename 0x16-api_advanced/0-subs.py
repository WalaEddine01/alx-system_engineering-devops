#!/usr/bin/python3
"""
this module contains a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers) for a given
"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API
    and returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(url, headers=header, allow_redirects=False)
    if res.status_code == 200:
        if res.json().get('data'):
            return res.json().get('data').get('subscribers')
        return 0
    return 0
