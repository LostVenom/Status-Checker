import os
import re
import pytz
import asyncio
import datetime

from pyrogram import Client, filters
from pyrogram.errors import FloodWait


app = Client(
    name = "TitanNetwrk",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)

TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_ID = int(os.environ["CHANNEL_ID"]) #CHANNEL_ID is for group/channel where checker will update the status.
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]
GRP_ID = os.environ.get("GRP_ID") #GRP_ID is for logs group where checker will send warnings of offline bots.

async def main_Lost():
    async with app:
            while True:
                print("☞ Checking Your Bots...")
                venom = f"**{(await app.get_chat(CHANNEL_ID)).title} 𝖡𝗈𝗍 𝖲𝗍𝖺𝗍𝗎𝗌 𝖴𝗉𝖽𝖺𝗍𝖾 :**"
                for bot in BOT_LIST:
                    await asyncio.sleep(7)
                    try:
                        bot_info = await app.get_users(bot)
                    except Exception:
                        bot_info = bot

                    try:
                        black = await app.send_message(bot, "/start")
                        aaa = black.id
                        await asyncio.sleep(15)
                        titan = app.get_chat_history(bot, limit = 1)
                        async for ccc in titan:
                            bbb = ccc.id
                        if aaa == bbb:
                            venom += f"\n\n⌬ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n⌥• **𝖲𝗍𝖺𝗍𝗎𝗌 : Dead 💀**"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(GRP_ID), f"**‼️ 𝖳𝗂𝗍𝖺𝗇 𝖡𝗈𝗍𝗌 𝖲𝗍𝖺𝗍𝗎𝗌 𝖠𝗅𝖾𝗋𝗍 ‼️**\n\n⌬**[{bot_info.first_name}](tg://user?id={bot_info.id})**\n⌥• **𝖲𝗍𝖺𝗍𝗎𝗌 : Dead 💀**\n\n @admin")
                                except Exception:...
                            await app.read_chat_history(bot)
                        else:
                            venom += f"\n\n⌬ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n⌥• **𝖲𝗍𝖺𝗍𝗎𝗌 : 𝖫𝗂𝗏𝖾 💨**"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        ttm = re.findall("\d{0,5}", str(e))
                        await asyncio.sleep(int(ttm))
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                venom += f"\n\n👾 𝖫𝖺𝗌𝗍 𝖴𝗉𝖽𝖺𝗍𝖾𝖽 𝗈𝗇 :\n**☞ {last_update}**\n\n          𝐵𝑒𝑠𝑡 𝑅𝑒𝑔𝑎𝑟𝑑𝑠:\n🎖𝑇𝐼𝑇𝐴𝑁 𝑁𝐸𝑇𝑊𝑂𝑅𝐾🎖"
                await app.edit_message_text(int(CHANNEL_ID), MESSAGE_ID, venom)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(3000)
                        
app.run(main_Lost())
