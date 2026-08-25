import time
from playwright.sync_api import sync_playwright
import re
import urllib.request


class InstagramStoryDownloader:
    """
    A class to automate downloading Instagram Stories using Playwright
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

            print("Checking if it's needed to click 'view story'...")
            try:
                page.get_by_role("button", name="View Story").click(timeout=5000)
                print("Button was clicked! Loading story...")
                
            except Exception:
                pass
            
            print("Waiting for image or video to appear...")
            try:
                page.wait_for_selector("video, img", timeout=15000)
                time.sleep(3) 
            except Exception as e:
                print(f"Unable to access the Instagram player: {e}")

            if(self.video_url is not None):
                print("Downloading video...")
                file_name = f"story_{target_profile}_{int(time.time())}.mp4"
                
                req = urllib.request.Request(self.video_url, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)'})
                with urllib.request.urlopen(req) as response, open(file_name, 'wb') as out_file:
                    out_file.write(response.read())
                    
                print(f"✅ Saved: {file_name}")
            elif(self.img_url is not None):
                print("Downloading image...")
                file_name = f"story_{target_profile}_{int(time.time())}.jpg"
                
                req = urllib.request.Request(self.img_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response, open(file_name, 'wb') as out_file:
                    out_file.write(response.read())
                print(f"✅ Saved: {file_name}")