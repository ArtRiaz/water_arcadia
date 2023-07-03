from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.reply import kb_menu, get_kb_menu, get_back
from aiogram.dispatcher.filters import Text


async def cmd_menu(message: types.Message):
    with open('logo.jpg', 'rb') as photo:
        await message.delete()
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo,
                             caption=f'<b>Вода «Arcadia» завдяки природному походження нашої води, вона не просто смачна '
                                     f'сама по собі, а й дарує незабутній смак усім вашим стравам та напоям.!!!</b>',
                             reply_markup=get_back())


def register_handlers_about(dp: Dispatcher):
    dp.register_message_handler(cmd_menu, Text(equals='Наша компанія'))
