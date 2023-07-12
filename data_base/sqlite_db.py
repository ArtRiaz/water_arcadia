import sqlite3 as sq
from create_bot import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery, Message
from aiogram import Dispatcher, types
from aiogram.utils.callback_data import CallbackData

cb = CallbackData('btn', 'type', 'id')
con = sq.connect("tg.db")
cur = con.cursor()


async def sql_start():
    cur.execute(
        'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT , img TEXT, name TEXT , '
        'description '
        'TEXT , price INTEGER)')
    cur.execute('CREATE TABLE IF NOT EXISTS cart (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, product_id '
                'INTEGER)')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER UNIQUE, name TEXT)')

    con.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO items(img, name, description, price) VALUES(?, ?, ?, ?)", tuple(data.values()))
        con.commit()


async def sql_read(message):
    for ret in cur.execute("SELECT * FROM items"):
        await bot.send_photo(message.from_user.id, ret[1], f'{ret[2]}\nОпис: {ret[3]}\nЦіна: {ret[4]} грн)',
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton("Додати у корзину", callback_data=f'btn:buy:{ret[0]}')))


async def sql_read2():
    return cur.execute('SELECT * FROM items').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM items WHERE description = (?)', (data,))
    con.commit()
