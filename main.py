# main.py
import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import admin_handlers, download_handlers
from utils.spotify_client import init_spotify
import logging

logging.basicConfig(level=logging.INFO)
app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    # register handlers
    await admin_handlers.register_handlers(app)
    await download_handlers.register_handlers(app)

    await app.start()
    print("Bot started")
    await app.idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
