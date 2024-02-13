#!/usr/bin/python3
"""
this module contains a function that queries
the Reddit API and returns the number of subscribers
"""

from requests import get


def top_ten(subreddit):
    """
    function that queries the Reddit API
    and returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    header = {
        "User-Agent": "Mozilla/5.0"
        }
    res = get(url=url, headers=header, allow_redirects=False)
    if res.status_code == 200:
        for post in res.json().get('data', {}).get('children', []):
            print(post['data']['title'])
    print(None)
