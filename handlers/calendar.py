from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.reply import get_back
from aiogram.dispatcher.filters import Text


async def cmd_calendar(message: types.Message):
    await message.answer('Мені потрібно розуміти яку функцію несе ця кнопка, що там повинно бути и т.д.', reply_markup=get_back())

def handler_calendar(dp:Dispatcher):
    dp.register_message_handler(cmd_calendar, Text(equals="Календар"))