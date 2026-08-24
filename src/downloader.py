import time
from playwright.sync_api import sync_playwright
import re
import urllib.request

class InstagramStoryDownloader:
    """
    A class to automate downloading Instagram Stories using Playwritght
    """
    def __init__(self,session_id: str):
        self.session_id = session_id
        self.video_url = None
        self.img_url = None
        

    def _intercept_request(self, request):
        url = request.url

        if(".mp4" in url and  "audio" not in url):
            url = re.sub(r"&bytestart=\d+", "", url)
            url = re.sub(r"&byteend=\d+", "", url)
            self.video_url = url
        elif(".jpg" in url and "1080x" in url):
            self.img_url = url


    def download_story(self, target_profile: str):
        with sync_playwright() as p:
            iPhone_13 = p.devices['iPhone 13']
            
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(**iPhone_13)
        
            context.add_cookies([
                {
                    'name': "sessionid",
                    'value': self.session_id,
                    'domain': '.instagram.com',
                    'path': '/'
                }
            ])

            
            page = context.new_page()
            page.on("request", self._intercept_request)
            page.goto(f"https://www.instagram.com/stories/{target_profile}")
            time.sleep(2)

            if(self.video_url is not None):
                urllib.request.urlretrieve(self.video_url, f"{target_profile}.story.{int(time.time())}.mp4")
            elif(self.img_url is not None):
                urllib.request.urlretrieve(self.img_url, f"{target_profile}_story_{int(time.time())}.jpg")
            time.sleep(2)

        
           


if __name__ == "__main__":
    ...



    

