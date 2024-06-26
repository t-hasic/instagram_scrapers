import os
import time
import random
import instaloader
from datetime import datetime
from dotenv import load_dotenv
from utils.get_metrics import get_metrics
from utils.byte_array import mp4_to_byte_array, store_byte_array

def switch_proxy(proxy):
    """
    
    Switches the proxy for the instaloader instance.

    Parameters:

    proxy (str): proxy to switch to

    Returns:

    None

    """
    os.environ['https_proxy'] = proxy

def scrape_usernames_posts(usernames, metrics = False, num_posts = None, proxies = None):
    """
    
    Scrapes the posts of a list of usernames and saves them in a directory.

    Parameters:

    usernames (list): list of usernames to scrape
    metrics (bool): if True, prints metrics for each username
    num_posts (int): number of posts to scrape for each username
    proxies (list): list of proxies to switch to

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
            num_files = 0
            total_delay = 0
            start_time = time.time()

        i = 0
        for post in profile.get_posts():
            L.download_post(post, target=path)
            # obtain metrics
            if metrics:
                path_metrics = get_metrics(path)
                num_videos += path_metrics[0]
                num_images += path_metrics[1]
                num_files += path_metrics[2]
            # move files to new directory
            results_path = f"./results_{timestamp}/{username}/post_{i}"
            os.system(f"mv {path} {results_path}")

            # convert mp4's to byte arrays
            for file in os.listdir(results_path):
                if file.endswith(".mp4"):
                    byte_array = mp4_to_byte_array(f"{results_path}/{file}")
                    file_without_extension = file.split(".")[0]
                    store_byte_array(byte_array, f"{results_path}/{file_without_extension}.bin")
                    os.system(f"rm {results_path}/{file}")

            i += 1
            if num_posts and i >= num_posts:
                break
            timeout = random.randint(1, 5)
            if metrics:
                total_delay += timeout
            time.sleep(timeout)
        # delete original directory
        os.system(f"rm -r {path}")
        if metrics:
            end_time = time.time()
        # print metrics
        if metrics:
            print("\n")
            print("-"*100)
            print(f"Metrics for {username}:\n")
            print(f"Number of videos: {num_videos}")
            print(f"Number of images: {num_images}")
            print(f"Collected {num_files} files in {end_time - start_time - total_delay} seconds.")
            print("-"*100)
        print(f"\nScraping complete for {username}!\n")

if __name__ == "__main__":
    scrape_usernames_posts(["beehiveboston"], metrics = True, num_posts = 3)