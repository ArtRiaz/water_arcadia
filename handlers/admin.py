from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text, Command
from data_base.sqlite_db import sql_add_command, sql_read2, sql_delete_command, con, cur
from keyboards.admin_reply import kb_admin, kb_admin_cancel
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from create_bot import support_ids
from mailing import bot_mailing
from aiogram.types.callback_query import CallbackQuery
from asyncio import sleep

ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# Получаем id текущего админа
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, "Вітаю тебе адмін👋", reply_markup=kb_admin())


async def cancel_admin(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply("Ok", reply_markup=kb_admin())


async def cmd_start_admin(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply("Завантаж фото",
                            reply_markup=kb_admin_cancel())


async def check_photo(message: types.Message):
    await message.reply('Це не фотография', reply_markup=kb_admin_cancel())


async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["photo"] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Введіть назву товару", reply_markup=kb_admin_cancel())


async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["name"] = message.text
        await FSMAdmin.next()
        await message.reply("Введіть опис", reply_markup=kb_admin_cancel())


async def load_desc(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["description"] = message.text
        await FSMAdmin.next()
        await message.reply("Ціна:", reply_markup=kb_admin_cancel())


async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["price"] = int(message.text) / 100
            print(data['price'])

        await sql_add_command(state)
        await message.answer("Товар створено", reply_markup=kb_admin())
        await state.finish()


#########################################################################################################################
async def del_callback_run(callback_query: types.CallbackQuery):
    await sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f"{callback_query.data.replace('del ', '')} видалена.", show_alert=True)


async def delete_items(message: types.Message):
    if message.from_user.id == ID:
        read = await sql_read2()
        print(read)
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[1], f'{ret[2]}\nОпис: {ret[3]}\nЦіна: {ret[4]} грн ')
            await bot.send_message(message.from_user.id, text='Видалити товар?', reply_markup=InlineKeyboardMarkup(). \
                                   add(
                InlineKeyboardButton(f'Видалити: {ret[3]}', callback_data=f'del {ret[3]}')))


########################################################################################################################

async def send_all(message: types.Message):
    if message.chat.id == ID:
        await message.answer(f'Введіть текст розсилки:')
        await bot_mailing.text.set()


async def mailing_text(message: types.Message, state: FSMContext):
    answer = message.text
    markup = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[
        InlineKeyboardButton(text='Додати фото', callback_data='add_photo'),
        InlineKeyboardButton(text='Далі', callback_data='next'),
        InlineKeyboardButton(text='Відмінить', callback_data='quit')
    ]])
    await state.update_data(text=answer)
    await message.answer(text=answer, reply_markup=markup)
    await bot_mailing.state.set()


async def next(callback: CallbackQuery, state: FSMContext):
    users = cur.execute('SELECT "user_id" FROM "users"').fetchone()
    print(users)
    data = await state.get_data()
    text = data.get('text')
    await state.finish()
    for i in users:
        await dp.bot.send_message(chat_id=i, text=text)
        await sleep(0.33)
    await callback.message.answer('Розсилка виконана', reply_markup=kb_admin())


async def add_photo(callback: CallbackQuery):
    await callback.message.answer('Прийшліть фото')
    await bot_mailing.photo.set()


async def mailing_send(message: types.Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    await state.update_data(photo=photo_file_id)
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    markup = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[
        InlineKeyboardButton(text='Далі', callback_data='next'),
        InlineKeyboardButton(text='Відмінить', callback_data='quit')
    ]])
    await message.answer_photo(photo=photo, caption=text, reply_markup=markup)


async def start_next(callback: CallbackQuery, state: FSMContext):
    users = cur.execute('SELECT "user_id" FROM "users"').fetchall()
    print(users)
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    await state.finish()
    for user in users:
        for i_photo in user:
            print(i_photo)
            await dp.bot.send_photo(chat_id=i_photo, photo=photo, caption=text)
            await sleep(0.33)
    await callback.message.answer('Розсилка виконана', reply_markup=kb_admin())


async def no_photo(message: types.Message):
    markup = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[
        InlineKeyboardButton(text='Відмінить', callback_data='quit')
    ]])
    await message.answer('Прийшліть фото', reply_markup=markup)


async def quit(callback: CallbackQuery, state: FSMContext):
    await state.finish()
    await callback.message.answer('Розсилка відмінена', reply_markup=kb_admin())


########################################################################################################################

async def stasistic(message: types.Message):
    result = cur.execute('SELECT "user_id" FROM "users"').fetchall()
    print(result)
    await message.answer(f'Кількість відвідувачів бота: {len(result)}')


def register_handlers_start_admin(dp: Dispatcher):
    dp.register_message_handler(make_changes_command, Text(equals='Admin', ignore_case=True))
    dp.register_message_handler(cancel_admin, Text(equals='Відмінити створення товару', ignore_case=True), state="*")
    dp.register_message_handler(cmd_start_admin, Text(equals='Завантажити товар'), state=None)
    dp.register_message_handler(check_photo, lambda message: not message.photo, state=FSMAdmin.photo)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_desc, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '))
    dp.register_message_handler(delete_items, Text(equals="Видалити"))
    dp.register_message_handler(send_all, Text(equals="Розсилання"))
    dp.register_message_handler(mailing_text, state=bot_mailing.text)
    dp.register_callback_query_handler(add_photo, text='add_photo', state=bot_mailing.state)
    dp.register_message_handler(mailing_send, state=bot_mailing.photo, content_types=types.ContentType.PHOTO)
    dp.register_message_handler(no_photo, state=bot_mailing.photo)
    dp.register_callback_query_handler(quit, text='quit',
                                       state=[bot_mailing.text, bot_mailing.photo, bot_mailing.state])
    dp.register_callback_query_handler(start_next, text='next', state=bot_mailing.photo)
    dp.register_callback_query_handler(next, text='next', state=bot_mailing.state)
    dp.register_message_handler(stasistic, Text(equals='Статистика'))
