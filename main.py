from src.downloader import InstagramStoryDownloader
from src import config
import sys


if __name__ == "__main__":
    downloader = InstagramStoryDownloader(config.SESSION_ID)
    
    if ( len(sys.argv) != 2):
        print("Usage: python main.py <target_profile>")
        sys.exit(1)

    target_profile = sys.argv[1]
    profile_lenght = len(target_profile)

    if profile_lenght < 2 or profile_lenght > 30:
        print("Error: targer profile name must be between 2 and 30 characters.")
        sys.exit(1)

    
    print(f"Starting download for profile: {target_profile}") 
    downloader.download_story(target_profile)