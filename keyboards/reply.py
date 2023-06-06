from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def kb_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton('Меню')
    ]])

    return kb


def get_kb_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton('Наша компанія'), KeyboardButton('Календар')
    ], [
        KeyboardButton('Зробити заказ'), KeyboardButton('Найчастіщі запитання')
    ], [
        KeyboardButton('Контакти'), KeyboardButton('Онлайн-консультація')
    ]

    ])

    return kb


def get_back():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton('Назад у головне  меню')
    ]])

    return kb
