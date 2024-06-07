import os
import time
import random
import instaloader
from datetime import datetime
from dotenv import load_dotenv
from utils.get_metrics import get_metrics

def scrape_username_highlights(usernames, metrics = False):
    """
    
    Scrapes the highlights of a list of usernames and saves them in a directory.

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
        print(f"\nDownloading highlights for {username}...\n")
        path = f"{username}_highlights"
        profile = instaloader.Profile.from_username(L.context, username)
        # make new directory for profile
        os.system(f"mkdir results_{timestamp}/{username}")
        if metrics:
            num_videos = 0
            num_images = 0
            num_highlights = 0
        for highlight in L.get_highlights(profile):
            print(f"\nDownloading highlight {highlight.title}...\n")
            # make new directory for highlight
            # convert highlight name to a valid directory name
            highlight_name = highlight.title.replace(" ", "_")
            highlight_path = f"results_{timestamp}/{username}/{highlight_name}"
            os.system(f"mkdir {highlight_path}")
            i = 0
            for item in highlight.get_items():
                L.download_storyitem(item, target=path)
                # obtain metrics
                if metrics:
                    path_metrics = get_metrics(path)
                    num_videos += path_metrics[0]
                    num_images += path_metrics[1]
                    num_highlights += path_metrics[2]
                # move files to new directory
                results_path = f"./{highlight_path}/{i}"
                os.system(f"mv {path} {results_path}")
                i += 1
                time.sleep(random.randint(1, 5))
        # remove original directory
        os.system(f"rm -r {path}")
        # print metrics
        if metrics:
            print("\n")
            print("-"*100)
            print(f"Metrics for {username}:\n")
            print(f"Number of videos: {num_videos}")
            print(f"Number of images: {num_images}")
            print(f"Number of highlights: {num_highlights}")
            print("-"*100)
        print(f"\nScraping complete for {username}!\n")

if __name__ == "__main__":
    scrape_username_highlights(["beehiveboston"], metrics = True)
