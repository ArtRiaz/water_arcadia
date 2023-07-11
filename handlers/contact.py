from aiogram import types, Dispatcher
from create_bot import bot, dp
from aiogram.dispatcher.filters import Text
from keyboards.inline import ikb_contact
from keyboards.reply import get_back


async def cmd_contact(message: types.Message):
    await message.answer("Як з нами зв'язатись:",reply_markup=get_back())
    await message.delete()
    await message.answer('Виберіть мережу або номер телефону:', reply_markup=ikb_contact())


def register_handler_contact(dp: Dispatcher):
    dp.register_message_handler(cmd_contact, Text(equals='Контакти'))
