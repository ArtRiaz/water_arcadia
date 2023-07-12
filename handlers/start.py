from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.reply import kb_menu, get_kb_menu
from aiogram.dispatcher.filters import Text
from data_base.sqlite_db import con, cur


async def cmd_start(message: types.Message):
    with open('arc.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo,
                             caption=f'<b>Вітаю Вас {message.from_user.full_name}!\n'
                                     f'Вода «Arcadia» завдяки природному походження нашої води, вона не просто смачна '
                                     f'сама по собі, а й дарує незабутній смак усім вашим стравам та напоям. '
                                     f'Основна наша мета – забезпечення якісною, смачною та чистою артезіанською '
                                     f'водою максимальної кількості клієнтів, як приватних осіб, так і підприємств, '
                                     f'офісів, організацій громадського харчування та інших.</b> '
                             , reply_markup=kb_menu())

        cur.execute('INSERT INTO users(user_id, name) VALUES(?, ?)', (message.chat.id, message.chat.first_name))
        cur.close()
        con.commit()
        con.close()


async def cmd_menu(message: types.Message):
    await message.answer('Управління меню', reply_markup=get_kb_menu())


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(cmd_menu, Text(equals='Меню'))
