#!/usr/bin/python3
"""
this module contains a function that queries the
Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit or None if invalid subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit or
    None if invalid subreddit.
    """
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Linux"},
        params={"limit": 10},
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    for children in response.json().get("data").get("children"):
        print(children.get("data").get("title"))


if __name__ == '__main__':
    top_ten('programming')
