#!/usr/bin/python3
"""
This Module contains a function that queries the Reddit API
and returns a list of the titles of the first 10 hot posts listed
for a given subreddit. If no results are found for the given subreddit,
the function should return None. The function should return a list of
None for an invalid subreddit. The function should return a list of the
titles of the hot articles without any duplicates.
The function should return a list of the titles of
the hot articles for a given subreddit.
"""
import requests


def _count_words(search_words, word_list, word_count=[]):
    for i in range(len(word_list)):
        for word in search_words:
            word = word.lower()
            if word_list[i] == word:
                word_count[i] += 1


def count_words(subreddit, word_list, word_count=[], page_after=""):
    """
    Recursive function that queries the Reddit API
    and returns a list of the titles of the first 10 hot
    posts listed for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None. The function should return a
    list of None for an invalid subreddit.
    The function should return a list of the titles of the hot
    articles without any duplicates. The function should return a
    list of the titles of the hot articles for a given subreddit.
    The function should return a list of the titles of the hot
    articles for a given subreddit.
    """
    headers = {'User-Agent': 'Linux'}
    word_list = [word.lower() for word in word_list]

    if not word_count:
        for _ in word_list:
            word_count.append(0)

    response = requests.get(
        'https://www.reddit.com/r/{}/hot.json'.format(subreddit),
        headers=headers,
        params={"after": page_after},
        allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json().get("data")
    after = data.get('after')

    for children in data.get("children"):
        title = children.get("data").get('title')
        search_words = [word for word in title.split()]
        _count_words(search_words, word_list, word_count)

    if after:
        count_words(subreddit, word_list, word_count, after)
        return

    counter = {}
    for key_word in set(word_list):
        i = word_list.index(key_word)
        if word_count[i] != 0:
            counter[word_list[i]] = \
                (word_count[i] * word_list.count(word_list[i]))

    for key, value in sorted(
            counter.items(), key=lambda x: (-x[1], x[0])
    ): print('{}: {}'.format(key, value))


if __name__ == '__main__':
    count_words('programming', ['python', 'java', 'c'])
