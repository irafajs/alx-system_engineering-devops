#!/usr/bin/python3
"""
Shebang to create a py script
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "LINUX DESKTOP"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title", "").lower()
            for word in word_list:
                if word.lower() in title:
                    count_dict[word] = count_dict.get(word, 0) + 1

        after = data["data"]["after"]
        if after:
            return count_words(subreddit, word_list, after, count_dict)
        else:
            sorted_results = sorted(
                    count_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_results:
                print(f"{word}: {count}")
