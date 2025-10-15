# config.py - put your secrets here (DO NOT COMMIT to public repo)
import os

API_ID = int(os.getenv("API_ID", "-25451030"))         # Telegram API ID
API_HASH = os.getenv("API_HASH", "9810f1e7387fc060f76b706844364819")   # Telegram API hash
BOT_TOKEN = os.getenv("BOT_TOKEN", "8309793588:AAGydmyqQwipdIcZ64u7ZUC93CQ07KJOWLo")     # Telegram bot token

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "a036a12471e440b89c25ff33626294af")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "02cc2c77d37043739c5345c1060d21bb")

# Admins: list of Telegram user IDs who can use admin commands
ADMINS = list(map(int, os.getenv("ADMINS", "8210377618").split(","))) if os.getenv("ADMINS") else [8210377618]

# Where downloads go
DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH", "./downloads")

# Whether to enable youtube downloads
ENABLE_YT_DOWNLOAD = os.getenv("ENABLE_YT_DOWNLOAD", "true").lower() in ("1", "true", "yes")

# Max file size to send via Telegram (bots can send up to ~50MB on free tier, but set smaller)
MAX_SEND_FILESIZE_MB = int(os.getenv("MAX_SEND_FILESIZE_MB", "45"))
