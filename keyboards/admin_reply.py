from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def kb_admin():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton('Завантажити товар')
    ], [KeyboardButton('Видалити')], ['Розсилання'], [
        KeyboardButton('Статистика')
    ], [
        KeyboardButton('Назад у головне  меню')
    ]])

    return kb


def kb_admin_cancel():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton('Відмінити створення товару')]])

    return kb
