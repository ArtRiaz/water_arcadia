from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.reply import get_back
from aiogram.dispatcher.filters import Text


async def cmd_order(message: types.Message):
    await message.answer('Ця кнопка знаходиться у стадії розробки...', reply_markup=get_back())

def handler_order(dp:Dispatcher):
    dp.register_message_handler(cmd_order, Text(equals="Зробити заказ"))