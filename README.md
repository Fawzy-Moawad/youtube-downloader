# 📥 YouTube Playlist Downloader

A **Python-based application** that allows users to **download entire YouTube playlists and videos** with ease. The script supports **automatic setup, private video authentication, and a fully portable experience.**

---

## 📌 Features

- ✅ **Download YouTube videos and playlists** 🎥  
- ✅ **Automatic setup & dependency installation** 🔄  
- ✅ **Choose a custom download folder** 📂  
- ✅ **Automatic FFmpeg detection & merging** 🔗  
- ✅ **Support for private videos (authentication via cookies)** 🔑  
- ✅ **Portable & works on Windows (no manual installation required)** 💻  

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/youtube-downloader.git
cd youtube-downloader
```

### 2️⃣ Run the Script (Everything is Automatic!)

Just **run** the script, and it will **automatically install** all dependencies!

```bash
python downloader.py
```

✅ The script will check for missing dependencies and install them automatically. No need to install anything manually!

---

## 🚀 Usage

### 1️⃣ Download Videos & Playlists

1. **Run the script**:
   ```bash
   python downloader.py
   ```
2. **Enter the YouTube URL** (Video or Playlist).
3. **Select a folder** to save the videos.
4. **The script will automatically download and merge video + audio.**

---

## 🔑 Downloading Private Videos

If your **playlist contains private videos**, you need to authenticate using **browser cookies**.

### 1️⃣ Extract YouTube Cookies

#### **Method 1: Automatic Cookie Extraction**

If using Chrome, run:

```bash
yt-dlp --cookies-from-browser chrome "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"
```

For Firefox, use:

```bash
yt-dlp --cookies-from-browser firefox "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"
```

#### **Method 2: Manual Cookie Export (More Reliable)**

1. **Install the `Get Cookies.txt` Chrome extension:**  
   👉 [Download Here](https://chrome.google.com/webstore/detail/get-cookies-txt/)  
2. **Open YouTube & log in.**
3. **Click the extension & export cookies.**
4. **Save the file as `youtube_cookies.txt` inside the project folder.**

✅ Now the script will **automatically detect** and use the cookies for downloading private videos!

---

## 🛠️ Troubleshooting

### ❌ FFmpeg Not Found

If you see this error:

```bash
ERROR: You have requested merging of multiple formats but ffmpeg is not installed.
```

Make sure:
- You downloaded **FFmpeg** and placed it in the `ffmpeg/` folder.
- The correct structure is: `ffmpeg/bin/ffmpeg.exe`

---

## 📁 Folder Structure

```bash
youtube-downloader/
│── downloader.py       # Main script
│── ffmpeg/             # FFmpeg folder (bin inside)
│── youtube_cookies.txt # (Optional) Saved cookies for private videos
│── requirements.txt     # Dependencies
│── README.md           # This file
```

---

## 📝 License

This project is **open-source** and available under the **MIT License**.

🚀 **Enjoy downloading your favorite playlists!** 🎥💾  
If you like this project, star ⭐ it on GitHub! 😊
