"""

Obtains the posts of a user profile and saves them in a directory.

"""
import os
import instaloader
from datetime import datetime
from dotenv import load_dotenv


if __name__ == "__main__":
    usernames = ["beehiveboston"]

    # Get instance
    L = instaloader.Instaloader()

    L.interactive_login("joe_smith_923") # (ask password on terminal) 

    for username in usernames:
        print(f"Downloading posts for {username}...")
        profile = instaloader.Profile.from_username(L.context, username)
        for post in profile.get_posts():
            timestamp = datetime.now().strftime('%Y-%m-%d')
            L.download_post(post, target=f"./results/{profile.username}_posts_{timestamp}")