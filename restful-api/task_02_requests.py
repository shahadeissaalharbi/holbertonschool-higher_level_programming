#!/usr/bin/python3
"""Module for consuming and processing data from the JSONPlaceholder API."""
import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print their titles.

    Prints the status code of the response, and if the request was
    successful, prints the title of every post returned by the API.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder and save them to a CSV file.

    Structures the fetched data into a list of dictionaries with keys
    'id', 'title', and 'body', then writes that data to posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        data = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"],
            }
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
