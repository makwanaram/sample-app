from pyrogram import filters
from pyrogram import Client as stark
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import LOGGER
from config import Config
import os
import sys
import traceback
from helper import log_error_to_telegram


@stark.on_message(filters.command(["start"]))
async def Start_msg(bot: stark , m: Message):
    if m.edit_date:
        return
    LOGGER.info("Start command received")
    try:
        await bot.send_photo(
        m.chat.id,
        photo="https://telegra.ph/file/cef3ef6ee69126c23bfe3.jpg",
        caption = "**Hi i am All in One Extractor Bot**.\n"
                                "Press **/pw** for **Physics Wallah**..\n\n"
                                "Press **/e1** for **E1 Coaching App**..\n\n"
                                "Press **/vidya** for **Vidya Bihar App**..\n\n"
                                "Press **/ocean** for **Ocean Gurukul App**..\n\n"
                                "Press **/winners** for **The Winners Institute**..\n\n"
                                "Press **/rgvikramjeet** for **Rgvikramjeet App**..\n\n"
                                "Press **/txt** for  **Ankit With Rojgar,**\n**The Mission Institute,**\n**The Last Exam App**..\n\n"
                                "Press **/cp** for **classplus appp**..\n\n"
                                "Press **/cw** for **careerwill app**..\n\n"
                                "Press **/khan** for **Khan Gs app**..\n\n"
                                "Press **/exampur** for ** Exampur app**..\n\n"
                                "Press **/samyak** for ** Samayak Ias**..\n\n"
                                "Press **/mgconcept** for **Mgconcept app**..\n\n"
                                "Press **/down** for **For Downloading Url lists**..\n\n"
                                "Press **/forward** To **Forward from One channel to others**..\n\n"
                                "**𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿 : 𝒞𝓇𝓎𝓅𝓉💞𝓈𝓉𝒶𝓇𝓀**")
    except Exception as e:
        LOGGER.error(f"Error in Start_msg: {e}")
        try:
            await log_error_to_telegram(bot, f"Error in Start_msg: {traceback.format_exc()}")
        except Exception as log_e:
            LOGGER.error(f'Failed to send error message to Telegram: {log_e}')
           


@stark.on_message(filters.command(["restart"]))
async def restart_handler(_, m):
    if m.edit_date:
        return
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@stark.on_message(filters.command(["log"]))
async def log_msg(bot: stark , m: Message):   
    if m.edit_date:
        return
    await bot.send_document(m.chat.id, "log.txt")
