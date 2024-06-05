"""

Obtains the highlights of a user profile and saves them in a directory.

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
        print(f"Downloading highlights for {username}...")
        timestamp = datetime.now().strftime('%Y-%m-%d')
        profile = instaloader.Profile.from_username(L.context, username)
        L.download_highlights(profile, filename_target=f"{profile.username}_stories_{timestamp}")