#!/usr/bin/python3
"""
Shebang to create a PY script
"""

import requests


def top_ten(subreddit):
    """return top ten of posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Linux desktop"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts[:10]:
            title = post.get("data", {}).get("title", "")
            print(title)
    else:
        print("None")
