#!/usr/bin/python3
"""
Shebang to create a PY script
"""


import requests


def number_of_subscribers(subreddit):
    """method to get mumber of sub on reddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "ubuntu_desktop"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers_count = data["data"]["subscribers"]
        return subscribers_count
    else:
        return 0
