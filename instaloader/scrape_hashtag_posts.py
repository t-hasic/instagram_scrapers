"""

Obtains posts associated with specified hashtag and saves them in a directory.

DOES NOT CURRENT WORK. SEE THIS GITHUB ISSUE: https://github.com/instaloader/instaloader/issues/2206

"""
import os
import instaloader
from datetime import datetime
from dotenv import load_dotenv


if __name__ == "__main__":
    limit = 10
    hashtags = ["flowers"]

    # Get instance
    L = instaloader.Instaloader()

    L.interactive_login("joe_smith_923") # (ask password on terminal) 

    for hashtag in hashtags:
        print(f"Downloading posts for #{hashtag}...")
        num = 1
        timestamp = datetime.now().strftime('%Y-%m-%d')
        hashtag = instaloader.Hashtag.from_name(L.context, hashtag)
        for post in hashtag.get_top_posts():
            if num > limit:
                break
            L.download_post(post, target=f"{hashtag.name}_posts_{timestamp}")
            num += 1
