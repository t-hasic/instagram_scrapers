import os

def get_metrics(folder_path):
    """
    
    Returns the number of videos, images, and highlights in a folder.

    Parameters:

    folder_path (str): path to folder containing highlights

    Returns:

    num_videos (int): number of videos in folder
    num_images (int): number of images in folder
    num_highlights (int): number of highlights in folder

    """

    num_videos = 0
    num_images = 0
    num_files = 0
    for file in os.listdir(folder_path):
        if file.endswith(".mp4"):
            num_videos += 1
            num_files += 1
        elif file.endswith(".jpg"):
            num_images += 1
            num_files += 1
    return num_videos, num_images, num_files