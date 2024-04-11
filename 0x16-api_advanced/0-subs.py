#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.
    Returns:
    - int: Number of subscribers, or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set a custom User-Agent to avoid being blocked
    headers = {'User-Agent': 'My User Agent'}

    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        
        # Check if the subreddit exists
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            # Subreddit does not exist or API response format changed
            return 0
    else:
        # Request failed, possibly due to invalid subreddit or other issues
        return 0