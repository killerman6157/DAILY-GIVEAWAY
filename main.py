import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from datetime import datetime, time
import asyncio
from config import BOT_TOKEN, CHANNEL_ID, GROUP_ID
from gender_detector import detect_gender
from db import add_entry, has_entered, count_gender, is_full, get_all_entries
from scheduler import schedule_tasks

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

MALE_LIMIT = 30
FEMALE_LIMIT = 20

# Helper to format the account details reply
def format_receipt(entry):
    return f"""
✅ An tura kudi zuwa:
Bank num: {entry['account_number']}
Bank name: {entry['bank_name']}
Name holder: {entry['holder_name']}
👤 Jinsi: {entry['gender'].capitalize()}
"""

# Message when user tries to enter twice
DUPLICATE_MESSAGE = """
⚠️ Ka riga ka sa account details naka.

📦 Idan kana cikin winners, zaka samu gift naka daga 10:00 zuwa 11:00PM.

🙏 Mun gode.  
🧕 Nine naku – Bashir Rabiu.
"""

@dp.message_handler(lambda msg: msg.chat.id == GROUP_ID)
async def collect_account_details(message: types.Message):
    user_id = message.from_user.id
    text = message.text

    if has_entered(user_id):
        await message.reply(DUPLICATE_MESSAGE)
        return

    # Try to extract account details
    try:
        lines = text.split("\n")
        account_number = lines[0].split(":")[-1].strip()
        bank_name = lines[1].split(":")[-1].strip()
        holder_name = lines[2].split(":")[-1].strip()
    except Exception:
        await message.reply("❌ Format ɗin bai daidai ba. Da fatan ka bi misali da kyau.")
        return

    gender = detect_gender(holder_name)

    if is_full(gender, MALE_LIMIT, FEMALE_LIMIT):
        await message.reply(f"❌ An kammala karɓar bayanan {gender}s.")
        return

    add_entry(user_id, account_number, bank_name, holder_name, gender)

    current_m = count_gender("male")
    current_f = count_gender("female")

    if current_m >= MALE_LIMIT and current_f >= FEMALE_LIMIT:
        await bot.send_message(GROUP_ID, 
            f"✅ An kammala karɓar account details:\n\n👩 Mata: {current_f}\n👨 Maza: {current_m}\n\n💸 Zaa tura musu kudi daga 10:00 zuwa 11:00PM. Mun gode 🙏")

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply("🤖 Giveaway bot na aiki. Jira lokaci ya yi.")

async def send_final_receipts():
    await asyncio.sleep(1)
    entries = get_all_entries()
    for entry in entries:
        await bot.send_message(GROUP_ID, format_receipt(entry))
        await asyncio.sleep(1)
    await bot.send_message(GROUP_ID, 
        """
🎁 Giveaway ya kammala!  
Admin @HausaEscrowSupport ya tura gift zuwa ga winners.

🙏 Mun gode da kuka kasance damu.  
🧕 Sunana Bashir Rabiu.
        """)

if __name__ == '__main__':
    schedule_tasks(bot)
    executor.start_polling(dp, skip_updates=True)
