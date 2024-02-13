#!/usr/bin/python3
"""
this module contains a function that queries
the Reddit API and returns the number of subscribers
"""

from requests import get

def top_ten(subreddit):
    """
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    header = {
        "User-Agent": "Mozilla/5.0"
    }
