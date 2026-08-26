# Instagram Story Downloader 📸

A Python-based, Object-Oriented tool that automates the downloading of Instagram Stories (videos and images) using Playwright.

Unlike standard scraping tools, this script does not rely on the official Instagram API or HTML parsing. Instead, it intercepts background network requests to fetch raw, uncompressed media links directly from Instagram's servers, helping to avoid common blocks with User-Agent spoofing.

## ✨ Features

* **Network Interception:** Captures raw `.mp4` and `.jpg` streams directly from network traffic.
* **Anti-Blocking Measures:** Emulates an iPhone 13 environment and uses a custom User-Agent during downloads to help prevent `403 Forbidden` errors.
* **Secure Configuration:** Uses `python-dotenv` to keep sensitive Session IDs out of the source code.


## ⚙️ Prerequisites

* Python 3.7+
* pip (Python package installer)

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Dawid0dihowski/instagram-story-downloader.git
cd instagram-story-downloader
```

### 2. Create and activate a virtual environment

**Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the required Python packages

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
playwright install
```
## 🔏 Configuration

To access stories, the script requires your Instagram `sessionid` cookie:

### How to get your `sessionid`:
1. Open your browser and log into [Instagram](https://www.instagram.com).
2. Open Developer Tools by pressing `F12` (or `Ctrl + Shift + I` / `Cmd + Option + I` on macOS).
3. Navigate to the **Application** tab (Chrome/Edge/Brave) or **Storage** tab (Firefox).
4. In the left sidebar, expand **Cookies** and select `https://www.instagram.com`.
5. Find the row with the name **`sessionid`** and copy its **Value**.

### Setup `.env` file:
1. Create a file named `.env` in the root directory.
2. Add your copied session ID:
   ```env
   INSTAGRAM_SESSION_ID=your_cookie_value_here
   ```
> **Note:** Never share your `.env` file or commit it to GitHub. It is already included in `.gitignore`.

## 💻 Usage

You can run the script directly from your terminal by passing the target profile name as an argument.

```bash
python main.py <target profile>
```

example

```bash
python main.py cristiano
```

The script will automatically launch a browser instance, handle the **"View Story"** confirmation, intercept the media URL, and save the file with a timestamp directly to your project folder.

## ⚠️ Disclaimer

This tool is for educational purposes only. Downloading content from Instagram may violate their Terms of Service.

Please respect user privacy and copyright laws. Do not use this tool to download or distribute content without the creator's permission.
