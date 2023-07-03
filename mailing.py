from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher


class bot_mailing(StatesGroup):
    text = State()
    state = State()
    photo = State()
