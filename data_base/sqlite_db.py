import sqlite3 as sq
from create_bot import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery, Message
from aiogram import Dispatcher, types
from aiogram.utils.callback_data import CallbackData

cb = CallbackData('btn', 'type', 'id')


def sql_start():
    global base, cur
    base = sq.connect('water.db')
    cur = base.cursor()
    if base:
        print('connection')
    base.execute(
        'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, img TEXT, name TEXT , description '
        'TEXT , price INTEGER)')
    base.execute('CREATE TABLE IF NOT EXISTS cart (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, product_id '
                 'INTEGER)')
    base.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, user_id INTEGER UNIQUE, name TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO items(img, name, description, price) VALUES(?, ?, ?, ?)", tuple(data.values()))
        base.commit()


# async def sql_add_cart(state):
#     cur.execute("INSERT INTO cart VALUES(?, ?, ?)", ('name', 'description', )
#     base.commit()


async def sql_read(message):
    for ret in cur.execute("SELECT * FROM items").fetchall():
        await bot.send_photo(message.from_user.id, ret[1], f'{ret[2]}\nОпис: {ret[3]}\nЦіна: {ret[4]} грн',
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton("Додати у корзину", callback_data=f'btn:buy:{ret[0]}')))




async def sql_read2():
    return cur.execute('SELECT * FROM items').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM items WHERE description == ?', (data,))
    base.commit()


