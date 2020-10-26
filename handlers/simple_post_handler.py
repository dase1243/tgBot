from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.SimplePost import SimplePost


@dp.message_handler(Command("/make_simple_post"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Вы начали создание простого поста.\n"
                         "Введите текст поста. \n\n")
    await SimplePost.s1_enter_post_text.set()


@dp.message_handler(state=SimplePost.s1_enter_post_text)
async def enter_post_text(message: types.Message, state: FSMContext):
    post_text = message.text

    # Ваирант 2 получения state
    # state = dp.current_state(chat=message.chat.id, user=message.from_user.id)

    await state.update_data(post_text=post_text)

    await message.answer("Вот как будет выглядеть поста")
    await SimplePost.s2_preview.set()


@dp.message_handler(state=SimplePost.s2_preview)
async def preview_simple_post(message: types.Message, state: FSMContext):
    data = await state.get_data()

    kb = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    make_post = types.KeyboardButton(text="Сделать пост")
    reset = types.KeyboardButton(text="Отменить создание поста")

    kb.add(make_post, reset)

    await message.answer(text=data.get("post_text"), reply_markup=kb)
    await SimplePost.s3_make_post.set()


@dp.message_handler(state=SimplePost.s3_make_post)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()

    if message.text == "Сделать пост":
        await dp.bot.send_message(chat_id="@testkamasutra", text=data.get("post_text"))
    elif message.text == "Отменить создание поста":
        pass
        # await state.finish()
    await state.finish()

    # Вариант завершения 2
    # await state.reset_state()

    # Вариант завершения 3 - без стирания данных в data
    # await state.reset_state(with_data=False)
