#!/usr/bin/python3

"""
Query Reddit API for titles of top ten posts of a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.
    Returns:
    - None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Ensure a custom User-Agent to prevent errors.
    headers = {'User-Agent': 'My User Agent'}

    try:
        # Send GET request to Reddit API
        response = requests.get(url, headers=headers)
        # Parse response as JSON
        data = response.json()

        # Check if 'data' key exists and 'children' key exists within it
        if 'data' in data and 'children' in data['data']:
            # Extract the first 10 posts
            posts = data['data']['children'][:10]
            # Print the titles of the posts
            for post in posts:
                print(post['data']['title'])
        else:
            # Print None if 'data' or 'children' key doesn't exist
            print(None)
    except requests.RequestException:
        # Print None if there's any exception during the request
        print(None)