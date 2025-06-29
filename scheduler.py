# scheduler.py

import asyncio
from datetime import datetime
from aiogram import Bot

from config import CHANNEL_ID, GROUP_ID

async def send_time_based_messages(bot: Bot):
    while True:
        now = datetime.now().strftime('%H:%M')

        if now == "20:30":
            await bot.send_message(GROUP_ID, "⏳ Saura mintuna 30 a fara sa account details. Ku shirya!")
        elif now == "20:50":
            await bot.send_message(GROUP_ID, "⏳ Saura mintuna 10 a fara sa account details. Ku shirya!")
        elif now == "21:00":
            await bot.send_message(GROUP_ID, "📥 It's time! Drop your account details here. 👇")
        elif now == "20:00":
            await bot.send_message(CHANNEL_ID, 
                "🎉 Yau zamuyi giveaway Mata 20, Maza 30. Kowa zai samu 1k/1!\n\n"
                "🕘 Lokacin Farawa: 9:00PM\n"
                "📤 Zamu fara turawa daga 10:00 zuwa 11:00PM\n\n"
                "🧾 Ku shirya a group din @BashGV da zaku sa account number dinku.\n\n"
                "Misali:\nBank num: 9131***779\nBank name: Opay\nName holder: Bashir Rabiu\n\n"
                "✂️ Ka rubuta ka ajje a clipboard\n"
                "⏰ Be fast saboda bot ne zai karbi bayanan. Allah ya bawa me rabo sa a 🙏"
            )

        await asyncio.sleep(60)  # check every minute

def schedule_tasks(bot: Bot):
    loop = asyncio.get_event_loop()
    loop.create_task(send_time_based_messages(bot))
