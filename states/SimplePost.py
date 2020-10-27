from aiogram.dispatcher.filters.state import StatesGroup, State


class SimplePost(StatesGroup):
    s1_enter_post_text = State()
    s2_make_post = State()
