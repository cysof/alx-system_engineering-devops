#!/usr/bin/python3

"""Query Reddit API, parses the title of all hot articles.
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
    - subreddit (str): The name of the subreddit.
    - word_list (list): List of keywords to count.
    - after (str): Identifier for the next page of results
      (used for pagination).
    - count_dict (dict): Dictionary to store the count of each keyword
      (used for recursion).

    Returns:
    - None
    """
    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Custom User-Agent to prevent errors.
    headers = {'User-Agent': 'custom-user-agent'}

    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    try:
        # Send GET request to Reddit API
        response = requests.get(url, headers=headers, params=params)
        # Parse response as JSON
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']

            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    # Check for occurrences of keyword in title
                    if f" {word} " in f" {title} ":
                        count_dict[word] = count_dict.get(word, 0) + 1

            if data['data']['after']:
                # Recursively call count_words for next page of results
                count_words(subreddit, word_list,
                            after=data['data']['after'], count_dict=count_dict)
            else:
                # Print the sorted count of keywords
                print_results(count_dict)
        else:
            print(None)
    except requests.RequestException:
        print(None)


def print_results(count_dict):
    """
    Prints the sorted count of keywords.

    Args:
    - count_dict (dict): Dictionary containing the count of each keyword.

    Returns:
    - None
    """
    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")