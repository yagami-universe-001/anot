# Telegram Music Downloader Bot

## Features
- Spotify search & metadata (requires Spotify Client ID & Secret)
- YouTube download to MP3 via yt-dlp (optional; configurable)
- Admin commands to change start message and start picture
- SQLite settings persistence

## Setup
1. Extract the zip.
2. (Optional) Create a `.env` or edit `config.py` if you want to change values.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run:
   ```
   python main.py
   ```

## Admin commands
- `/setstartmsg <text>` — set start message (admin only)
- Reply to a photo with `/setstartpic` — set start picture
- `/getstartmsg` `/getstartpic` — view current values

## Usage
- `/spotify <query>` — search Spotify (returns metadata + preview)
- `/search <query>` — friendly wrapper for Spotify
- `/yt <youtube_url>` — download audio from YouTube (if enabled)

## Legal
Use this bot only for content you have rights to. Downloading copyrighted content without permission may be illegal.
