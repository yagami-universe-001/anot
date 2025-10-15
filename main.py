# main.py
import asyncio
import logging
import sys
from pyrogram import Client
from pyrogram.errors import BadMsgNotification
from config import API_ID, API_HASH, BOT_TOKEN

logging.basicConfig(level=logging.INFO)

# Check for placeholder credentials
if not BOT_TOKEN or BOT_TOKEN == "8309793588:AAGydmyqQwipdIcZ64u7ZUC93CQ07KJOWLo":
    logging.error("ERROR: Invalid or placeholder BOT_TOKEN.")
    logging.error("Please set your bot token in config.py or as an environment variable.")
    sys.exit(1)

try:
    from handlers import admin_handlers, download_handlers
except ModuleNotFoundError:
    logging.error("ERROR: 'handlers' directory is missing or not a proper package.")
    logging.error("Please ensure the 'handlers' directory exists and contains '__init__.py'.")
    sys.exit(1)


app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    # register handlers
    await admin_handlers.register_handlers(app)
    await download_handlers.register_handlers(app)

    try:
        await app.start()
        logging.info("Bot started successfully!")
        await app.idle()
    except BadMsgNotification as e:
        logging.error(f"Pyrogram Error: {e}")
        logging.error(
            "This could be due to an invalid BOT_TOKEN or API credentials. "
            "Please verify them in your config.py or environment variables. "
            "It can also be caused by system time being out of sync."
        )
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        if app.is_initialized and app.is_connected:
            await app.stop()
        logging.info("Bot stopped.")

if __name__ == "__main__":
    asyncio.run(main())
