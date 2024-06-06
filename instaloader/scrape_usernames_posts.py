import os
import time
import random
import instaloader
from datetime import datetime
from dotenv import load_dotenv
from utils.get_metrics import get_metrics

def scrape_usernames_posts(usernames, metrics = False, num_posts = None):
    """
    
    Scrapes the posts of a list of usernames and saves them in a directory.

    Parameters:

    usernames (list): list of usernames to scrape
    metrics (bool): if True, prints metrics for each username
    num_posts (int): number of posts to scrape for each username

    Returns:

    None

    """
    # Get instance
    L = instaloader.Instaloader()

    # create results directory
    timestamp = datetime.now().strftime('%Y-%m-%d')
    os.system(f"mkdir results_{timestamp}")

    for username in usernames:
        print(f"\nDownloading posts for {username}...\n")
        path = f"{username}_posts"
        profile = instaloader.Profile.from_username(L.context, username)

        # make new directory for profile
        os.system(f"mkdir results_{timestamp}/{username}")

        if metrics:
            num_videos = 0
            num_images = 0
            num_highlights = 0

        i = 0
        for post in profile.get_posts():
            L.download_post(post, target=path)
            # obtain metrics
            if metrics:
                path_metrics = get_metrics(path)
                num_videos += path_metrics[0]
                num_images += path_metrics[1]
                num_highlights += path_metrics[2]
            # move files to new directory
            results_path = f"./results_{timestamp}/{username}/post_{i}"
            os.system(f"mv {path} {results_path}")
            i += 1
            if num_posts and i >= num_posts:
                break
            time.sleep(random.randint(1, 5))
        # delete original directory
        os.system(f"rm -r {path}")
        # print metrics
        if metrics:
            print("\n")
            print("-"*100)
            print(f"Metrics for {username}:\n")
            print(f"Number of videos: {num_videos}")
            print(f"Number of images: {num_images}")
            print(f"Total files: {num_highlights}")
            print("-"*100)
        print(f"\nScraping complete for {username}!\n")

if __name__ == "__main__":
    scrape_usernames_posts(["beehiveboston", "royaleboston"], metrics = True, num_posts = 3)