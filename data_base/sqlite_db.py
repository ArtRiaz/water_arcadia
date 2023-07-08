import asyncpg
from create_bot import dp, bot, DATABASE_URL
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery, Message
from aiogram import Dispatcher, types
from aiogram.utils.callback_data import CallbackData

cb = CallbackData('btn', 'type', 'id')


async def sql_start():
    global con
    con = await asyncpg.connect(DATABASE_URL)
    if con:
        print('connection')
    await con.execute(
        'CREATE TABLE IF NOT EXISTS items (id  serial  PRIMARY KEY, img VARCHAR(300), name VARCHAR(200) , '
        'description '
        'VARCHAR(1000) , price INTEGER NOT NULL)')
    await con.execute('CREATE TABLE IF NOT EXISTS cart (id  serial PRIMARY KEY, user_id INTEGER, product_id '
                      'INTEGER NOT NULL)')
    await con.execute(
        'CREATE TABLE IF NOT EXISTS users(id  serial  PRIMARY KEY, user_id INTEGER UNIQUE, name TEXT NOT NULL)')


async def sql_add_command(state):
    async with state.proxy() as data:
        await con.execute("INSERT INTO items(img, name, description, price) VALUES($1, $2, $3, $4)", data['photo'],
                          data['name'], data['description'], data['price'])


async def sql_read(message):
    global counter
    async with con.transaction():
        async for ret in con.cursor("SELECT * FROM items"):
            await bot.send_photo(message.from_user.id, ret[1], f'{ret[2]}\nОпис: {ret[3]}\nЦіна: {ret[4]} грн)',
                                 reply_markup=InlineKeyboardMarkup().add(
                                     InlineKeyboardButton("Додати у корзину", callback_data=f'btn:buy:{ret[0]}')))






async def sql_read2():
    return await con.fetch('SELECT * FROM items')


async def sql_delete_command(data):
    await con.execute('DELETE FROM items WHERE description = ($1)', data)
