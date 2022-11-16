from os import environ

from aiogram import Dispatcher
from aiogram import Bot
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from connect_ad import connect_ad
from connect_db import connect_db
from exception_list import get_except_chat_id
from keyboard_admin import button_case_admin

REDIS_DB_URL = environ['REDIS_DB_URL']  # Адрес БД Redis
REDIS_DB_PORT = int(environ["REDIS_DB_PORT"])
BOT_ID = int(environ["BOT_ID"])

storage = RedisStorage2(REDIS_DB_URL, REDIS_DB_PORT, db=5, pool_size=10, prefix='my_fsm_key')
bot = Bot(token=environ["TELEGRAM_TOKEN"])
dp = Dispatcher(bot, storage=storage)

db = connect_db()
ldap = connect_ad()


async def check_users(all_participants: list, chat_id: int, admin_id: int) -> None:

    for user_id in all_participants:
        except_user = get_except_chat_id(user_id.id)   # кортеж исключений из ID чатов
        if user_id.id == BOT_ID or user_id.id == admin_id:
            continue

        if except_user[0] and chat_id in except_user[0]:
            await bot.send_message(chat_id=admin_id,
                                   text=f"{user_id.id} name: {user_id.username} в списке исключения",
                                   reply_markup=button_case_admin)

        else:
            try:
                await bot.kick_chat_member(chat_id, user_id.id)
                await bot.unban_chat_member(chat_id, user_id.id)
                await bot.send_message(chat_id=admin_id,
                                       text=f"{user_id.id} {user_id.username} исключен из группы {chat_id}",
                                       reply_markup=button_case_admin)
            except Exception as e:
                continue
