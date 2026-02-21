import asyncio
from config import POSTS_PER_DAY
from database import get_unposted, mark_posted
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def scheduler(bot, channel):
    delay = int(86400 / POSTS_PER_DAY)

    while True:
        data = get_unposted()
        if data:
            pid, image, prompt, description = data
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="📋 Скопировать промт", callback_data=f"copy|{pid}")]
            ])
            caption = f"""📸 AI Prompt

Источник: {description}

Промт:
{prompt}
"""
            await bot.send_photo(channel, image, caption=caption, reply_markup=kb)
            mark_posted(pid)

        await asyncio.sleep(delay)
