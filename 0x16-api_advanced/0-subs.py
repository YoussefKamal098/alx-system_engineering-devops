#!/usr/bin/python3
"""
this module contains a function that queries the Reddit API and returns the
total number of subscribers for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "Linux"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')

    return 0


if __name__ == '__main__':
    print(number_of_subscribers('programming'))
