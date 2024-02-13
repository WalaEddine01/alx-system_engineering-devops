#!/usr/bin/python3
"""
this module contains a function that queries
the Reddit API and returns the number of subscribers
"""
from requests import get


header = {
    "User-Agent": "Mozilla/5.0"
    }


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    param = {'after': after}
    res = get(url=url, headers=header, allow_redirects=False, params=param)
    if res.status_code == 200:
        for post in res.json().get('data', {}).get('children', []):
            hot_list.append(post.get('data', {}).get('title'))
        if res.json().get('data', {}).get('after'):
            return recurse(subreddit, hot_list,
                           after=res.json().get('data', {}).get('after'))
        return hot_list
    return None
