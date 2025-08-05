import os
from config import Config
from pyrogram import Client, idle
import asyncio, logging
import tgcrypto
from pyromod import listen
from logging.handlers import RotatingFileHandler
import traceback
from helper import log_error_to_telegram

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "log.txt", maxBytes=5000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

# Auth Users
AUTH_USERS = [ int(chat) for chat in Config.AUTH_USERS.split(",") if chat != '']

# Prefixes 
prefixes = ["/", "~", "?", "!"]

plugins = dict(root="plugins")

async def initialize_bot():
    try:
        bot = Client(
            "StarkBot",
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            sleep_threshold=20,
            plugins=plugins,
            workers=50
        )
        return bot # Return the bot instance if initialization is successful
    except Exception as e:
        LOGGER.error(f"Error during bot initialization: {e}")
        try:
           await log_error_to_telegram(LOGGER, None, f"Error during bot initialization: {traceback.format_exc()}") # Pass None for bot if it failed to initialize
        except Exception as log_e:
           LOGGER.error(f"Failed to send initialization error to Telegram: {log_e}")
        return None # Return None if initialization failed

async def main():
    bot = await initialize_bot() # Await the initialization
    if bot is None:
        LOGGER.error("Bot initialization failed. Exiting.")
        return # Exit if bot initialization failed

    try:
        await bot.start()
        bot_info  = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started (c) STARKBOT --->")
        await idle()
    except Exception as e:
        LOGGER.error(f"Error during bot execution: {e}")
        try:
           await log_error_to_telegram(LOGGER, bot, f"Error during bot execution: {traceback.format_exc()}")
        except Exception as log_e:
           LOGGER.error(f"Failed to send execution error to Telegram: {log_e}")

    LOGGER.info(f"<---Bot Stopped-->")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
