import os
import requests
import m3u8
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from Crypto.Cipher import AES

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

bot = Client("drm_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@bot.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply("👋 Send /download <m3u8_url> to download Classplus DRM video.")

@bot.on_message(filters.command("download"))
async def download(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Please provide the `.m3u8` link.")

    m3u8_url = message.command[1]
    await message.reply("⏳ Processing...")

    try:
        os.makedirs("segments", exist_ok=True)
        playlist = m3u8.load(m3u8_url)
        key_url = playlist.keys[0].uri
        key = requests.get(key_url).content
        segments = playlist.segments

        for i, segment in enumerate(segments):
            uri = segment.absolute_uri
            iv = segment.key.iv
            if iv is None:
                iv = (i+1).to_bytes(16, byteorder='big')
            else:
                iv = bytes.fromhex(iv.replace("0x", "").zfill(32))
            data = requests.get(uri).content
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(data)
            with open(f"segments/seg_{i:05d}.ts", "wb") as f:
                f.write(decrypted)

        with open("output.ts", "wb") as merged:
            for i in range(len(segments)):
                with open(f"segments/seg_{i:05d}.ts", "rb") as f:
                    merged.write(f.read())

        os.system("ffmpeg -y -i output.ts -c copy final.mp4")
        await message.reply_document("final.mp4", caption="✅ Here is your video.")

    except Exception as e:
        await message.reply(f"❌ Error: {str(e)}")
    finally:
        for f in ["output.ts", "final.mp4"]:
            if os.path.exists(f):
                os.remove(f)
        if os.path.exists("segments"):
            for f in os.listdir("segments"):
                os.remove(f"segments/{f}")
            os.rmdir("segments")

bot.run()
