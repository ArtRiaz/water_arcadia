from aiogram.types import CallbackQuery
from create_bot import bot, dp
from aiogram import Dispatcher
from keyboards.reply import get_back


async def send_geo(callback: CallbackQuery):
    await callback.message.delete()
    await callback.bot.send_location(chat_id=callback.from_user.id,
                                     latitude=46.4698845,
                                     longitude=30.7390622,
                                     reply_markup=get_back()
                                     )


async def send_phone(callback: CallbackQuery):
    await callback.message.delete()
    await callback.bot.send_contact(chat_id=callback.from_user.id,
                                    phone_number='+38068-555-77-12',
                                    first_name='Замовлення води',
                                    reply_markup=get_back())


def register_inline_menu(dp: Dispatcher):
    dp.register_callback_query_handler(send_geo, text='Геолокация')
    dp.register_callback_query_handler(send_phone, text='Вызов')
