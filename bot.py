from pyrogram import Client
from pyrogram.errors import Flood
import asyncio
import os
###################################################################################################
bot_path = os.path.dirname(os.path.abspath(__file__))
api_id = "<paste_app_id_here>"
api_hash = "<paste_app_hash_here>"
bot = Client("Grabber", api_id=api_id, api_hash=api_hash)
chat_id = "<paste_chat_id_here>"
###################################################################################################
async def main():
    media_types = {
        "photo": ".png",
        "video": ".mp4",
        "animation": ".gif",
        "voice": ".ogg",
        "video_note": ".mp4",
        "audio": ".mp3",
        "sticker": ".webp",
    }
    async with bot:
        async for message in bot.get_chat_history(chat_id):
            try:
                if message.media is not None:
                    file_ext = media_types.get(message.media.value)
                    if file_ext:
                        await bot.download_media(message, file_name=f"{message.id}{file_ext}")
                        print(f"downloaded {message.media.value}")
            except Flood as e:
                await asyncio.sleep(e)
###################################################################################################
if __name__ == "__main__":
    print("Bot started")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()