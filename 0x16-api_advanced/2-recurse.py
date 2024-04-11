#!/usr/bin/python3

"""Recursive function module that queries Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    """Recursively fetches titles of hot posts from a subreddit.

    Args:
    - subreddit (str): The name of the subreddit.
    - hot_list (list): List to store the titles of hot posts
      (used for recursion).
    - count (int): The number of posts fetched in the current request
      (used for pagination).
    - after (str): Identifier for the next page of results
      (used for pagination).

    Returns:
    - list or None: A list containing titles of hot posts or None if no
      results are found.
    """

    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    query = f'?count={count}&after={after}'
    try:
        if count == 0 and after == "":
            url = endpoint
        else:
            url = endpoint + query
        # Send GET request to Reddit API
        response = requests.get(url, headers={"User-Agent": "My User Agent"},
                                allow_redirects=False)
        # Extract children titles from response JSON
        childrens = response.json().get("data").get("children")
        for post in childrens:
            # Append title to hot_list
            hot_list.append(post.get("data").get("title"))
        # Get count and after for pagination
        count = response.json().get("data").get("dist")
        after = response.json().get("data").get("after")
        # Recursively call the function if there are more posts
        if count != 0 and after is not None:
            return recurse(subreddit, hot_list=hot_list, count=count,
                           after=after)
        else:
            return hot_list  # Return hot_list if no more posts
    except Exception:
        return None  # Return None if there's any exception