from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


cancel = KeyboardButton('/отмена')
upload = KeyboardButton('/добавить')
delete = KeyboardButton('/удалить')
button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(cancel).add(upload).add(delete)
