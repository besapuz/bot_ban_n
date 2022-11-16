from os import environ

from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.utils import executor

from handlers import register_handler_client

storage = MemoryStorage()
bot = Bot(token=environ["TELEGRAM_TOKEN"])
dp = Dispatcher(bot, storage=storage)


async def on_startup(_):
    print("Бот вышел в эфир")


register_handler_client(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
