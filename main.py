from src.downloader import InstagramStoryDownloader
from src import config


if __name__ == "__main__":
    downloader = InstagramStoryDownloader(config.SESSION_ID)
    downloader.download_story("dodaqueen")