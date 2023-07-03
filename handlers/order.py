from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.reply import get_back
from aiogram.dispatcher.filters import Text
from data_base.sqlite_db import sql_read


async def cmd_order(message: types.Message):
    await message.answer('<b>Зробити заказ:</b>', reply_markup=get_back())
    await sql_read(message)


def handler_order(dp: Dispatcher):
    dp.register_message_handler(cmd_order, Text(equals="Зробити заказ"))
