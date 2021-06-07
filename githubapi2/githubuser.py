import sys
import requests

GITHUB_API = "https://api.github.com"

def get_username():
    return str(input("Username: "))


def get_user_details(username):
    return requests.get(f"{GITHUB_API}/users/{username}").json()


def print_data(user_details):
    print(user_details)

def run():
    username = get_username()
    user_details = get_user_details(username)
    print_data(user_details)


if __name__ == "__main__":
    run()
