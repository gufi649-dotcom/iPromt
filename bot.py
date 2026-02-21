import asyncio
from aiogram import Bot, Dispatcher, types
from config import BOT_TOKEN, CHANNEL_ID
from scheduler import scheduler
from parsers import run_all_parsers

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.callback_query()
async def copy_prompt(callback: types.CallbackQuery):
    await callback.message.answer(callback.message.caption)

async def parser_loop():
    while True:
        run_all_parsers()
        await asyncio.sleep(3600)

async def main():
    asyncio.create_task(parser_loop())
    asyncio.create_task(scheduler(bot, CHANNEL_ID))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
