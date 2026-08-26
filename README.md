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

## 🔐 Configuration

1. Create a file named `.env` in the root directory.
2. Add your Instagram Session ID to the file:

```env
INSTAGRAM_SESSION_ID=your_cookie_value_here
```

> **Note:** Never share your `.env` file or commit it to GitHub. It is already included in `.gitignore`.

## 💻 Usage

Currently, the target profile is configured inside the `main.py` file.

Open `main.py` and change the profile name in the `download_story` method, then run:

```bash
python main.py
```

The script will automatically launch a browser instance, handle the **"View Story"** confirmation, intercept the media URL, and save the file with a timestamp directly to your project folder.

## ⚠️ Disclaimer

This tool is for educational purposes only. Downloading content from Instagram may violate their Terms of Service.

Please respect user privacy and copyright laws. Do not use this tool to download or distribute content without the creator's permission.
