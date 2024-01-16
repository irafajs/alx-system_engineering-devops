#!/usr/bin/python3
"""
Shebang to create a PY script
"""


import requests


def recurse(subreddit, hot_list=None, after=None):
    """recursivily request data from reddit API"""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "LINUX DESKTOP"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            return hot_list
        else:
            titles = [post.get("data", {}).get("title", "") for post in posts]
            hot_list.extend(titles)
            after = data["data"]["after"]
            return recurse(subreddit, hot_list, after)
    else:
        return hot_list
