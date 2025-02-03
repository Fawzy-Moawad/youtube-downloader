import os
import sys
import subprocess
import tkinter as tk
from tkinter import filedialog
from yt_dlp import YoutubeDL

# Constants
COOKIES_FILE = "youtube_cookies.txt"
FFMPEG_DIR = "ffmpeg/bin/ffmpeg.exe"
DEFAULT_SAVE_PATH = os.path.expanduser("~/Downloads/Videos")

# Fake a Browser User-Agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"

def install_dependencies():
    """Ensure all dependencies are installed automatically."""
    try:
        __import__("yt_dlp")
    except ImportError:
        print("🔄 Installing yt-dlp...")
        subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp"], check=True)

def select_download_folder():
    """Let user select a folder to save videos."""
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="Select a folder to save videos")
    return folder if folder else DEFAULT_SAVE_PATH

def check_cookies():
    """Ensure cookies file exists, if not, extract them automatically from Chrome."""
    if not os.path.exists(COOKIES_FILE):
        print("🔍 Extracting YouTube cookies from Chrome...")
        try:
            subprocess.run(["yt-dlp", "--cookies-from-browser", "chrome", "--print-to-file", COOKIES_FILE], check=True)
            print("✅ Cookies extracted successfully!")
        except Exception:
            print("⚠️ Failed to extract cookies. Make sure Chrome is open and logged into YouTube.")
            print("👉 Follow these steps:\n"
                  "1️⃣ Install the 'Get Cookies.txt' Chrome Extension.\n"
                  "2️⃣ Open YouTube & log in.\n"
                  "3️⃣ Click the extension & export cookies to `youtube_cookies.txt` inside this folder.")
            sys.exit(1)

def download_videos(video_url, save_path):
    """Download YouTube videos with authentication and error handling."""
    print(f"📂 Saving videos to: {save_path}")

    ydl_opts = {
        "outtmpl": os.path.join(save_path, "%(title)s.%(ext)s"),
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "ffmpeg_location": FFMPEG_DIR if os.path.exists(FFMPEG_DIR) else None,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "cookiefile": COOKIES_FILE if os.path.exists(COOKIES_FILE) else None,
        "quiet": False,
        "noplaylist": False,
        "headers": {"User-Agent": USER_AGENT},  # Pretend to be a real browser
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
            print(f"✅ Download complete! Videos saved in: {save_path}")
            display_fm_ascii()  # Display "F M" after download completes
        except Exception as e:
            print(f"❌ ERROR: {e}")
            print("⚠️ Try re-exporting cookies or using a different network.")

def display_fm_ascii():
    """Display 'F M' using binary numbers (1 and 0)."""
    fm_ascii = """
    
    11111      000   000
    1          0 0   0 0
    11111      0  0 0  0
    1          0   0   0
    1          0       0
    
🚀 Coded by Fawzy Moawad
🔗 Visit: https://www.fawzymoawad.com for more source codes
    """
    print(fm_ascii)

if __name__ == "__main__":
    # Step 1: Install dependencies
    install_dependencies()

    # Step 2: Ensure cookies exist
    check_cookies()

    # Step 3: Ask for YouTube URL & Save Location
    video_url = input("Enter YouTube Video or Playlist URL: ").strip()
    save_path = select_download_folder()

    # Step 4: Download Videos
    download_videos(video_url, save_path)
