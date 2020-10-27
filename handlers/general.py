from aiogram.types import Message
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("start"))
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    create_post = types.KeyboardButton(text="Создать пост")
    await message.answer(text="Добро пожалуовать в бота по созданию постов", reply_markup=keyboard)


@dp.message_handler()
async def echo_message(message: Message):
    await message.reply(text=message.text)
