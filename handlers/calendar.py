from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.reply import get_back
from aiogram.dispatcher.filters import Text


async def cmd_calendar(message: types.Message):
    with open('logo.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption='<b>Ми працюєм кожен день з 9:00 по 19:00</b>', reply_markup=get_back())


def handler_calendar(dp: Dispatcher):
    dp.register_message_handler(cmd_calendar, Text(equals="Режим роботи"))
