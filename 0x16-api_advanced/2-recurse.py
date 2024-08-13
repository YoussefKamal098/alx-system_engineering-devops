#!/usr/bin/python3
"""
This Module contains a recursive function that queries the
Reddit API and returns a list containing the titles of all
hot articles for a given subreddit. If no results are found for
the given subreddit, the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.
    """
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Linux"},
        params={"after": after},
    )

    if response.status_code != 200:
        return None

    for children in response.json().get("data").get("children"):
        hot_list.append(children.get("data").get("title"))

    after = response.json().get("data").get("after")
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)


if __name__ == '__main__':
    recurse('programming')
