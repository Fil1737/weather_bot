import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from bot import handlers


async def start():
    load_dotenv()
    bot = Bot(os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    print(f"старт")

    dp.include_routers(
        handlers.user.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start())