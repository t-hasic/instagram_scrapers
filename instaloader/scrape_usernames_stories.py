import os
import time
import random
import instaloader
from datetime import datetime
from dotenv import load_dotenv
from utils.get_metrics import get_metrics

def scrape_usernames_stories(usernames, metrics = False):
    """
    
    Scrapes the stories of a list of usernames and saves them in a directory.

    Parameters:

    usernames (list): list of usernames to scrape
    metrics (bool): if True, prints metrics for each username

    Returns:

    None

    """
    # Scraper account username
    USERNAME = ""
    # Get instance
    L = instaloader.Instaloader()
    L.interactive_login(USERNAME) # (ask password on terminal)

    # create results directory
    timestamp = datetime.now().strftime('%Y-%m-%d')
    os.system(f"mkdir results_{timestamp}")

    for username in usernames:
        print(f"\nDownloading stories for {username}...\n")
        path = f"{username}_stories"
        # make new directory for profile
        os.system(f"mkdir results_{timestamp}/{username}")
        timestamp = datetime.now().strftime('%Y-%m-%d')
        profile = instaloader.Profile.from_username(L.context, username)
        L.download_stories([profile], filename_target=path)
        # obtain metrics
        if metrics:
            path_metrics = get_metrics(path)
            num_videos = path_metrics[0]
            num_images = path_metrics[1]
            num_stories = path_metrics[2]
        # move files to new directory
        os.system(f"mv {path} results_{timestamp}/{username}")
        # remove original directory
        os.system(f"rm -r {path}")
        # print metrics
        if metrics:
            print("\n")
            print("-"*100)
            print(f"Metrics for {username}:\n")
            print(f"Number of videos: {num_videos}")
            print(f"Number of images: {num_images}")
            print(f"Number of stories: {num_stories}")
            print("-"*100)
        print(f"\nScraping complete for {username}!\n")
        time.sleep(random.randint(1, 5))

if __name__ == "__main__":
    scrape_usernames_stories(["beehiveboston"], metrics = True)