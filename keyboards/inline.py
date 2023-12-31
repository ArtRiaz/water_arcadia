from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def ikb_contact():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('www.arcadia.od.ua', url='https://www.arcadia.od.ua/')
    ], [InlineKeyboardButton('Інстаграм', url='https://www.instagram.com/artemriazantsev22/')], [
        InlineKeyboardButton('Геолокація', callback_data='Геолокация')
    ], [
        InlineKeyboardButton('+38(068)-555-77-12', callback_data='Вызов')
    ]])

    return ikb


def ikb_question():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('Як зробити замовлення води?', callback_data="1")
    ], [InlineKeyboardButton('Де можна отримать інформацію про нас?', callback_data="2")], [
        InlineKeyboardButton('Як можна замовити доставку?', callback_data="3")
    ], [
        InlineKeyboardButton("Як зв'язатись з нами?", callback_data="4")
    ]])

    return ikb


def ikb_question_order():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton("Наш сайт", url='http://www.arcadia.od.ua/')
    ], [InlineKeyboardButton("Зробити заказ на боті", callback_data="order_bot")],[InlineKeyboardButton("Відміна", callback_data="cancel")]])

    return ikb


def ikb_question_info():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton("Наш сайт", url='http://www.arcadia.od.ua/')
    ], [InlineKeyboardButton("Наша компанія", callback_data="info_bot")], [
        InlineKeyboardButton("Відміна", callback_data="cancel")
    ]])

    return ikb

def ikb_question_contact():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton("Наш сайт", url='http://www.arcadia.od.ua/')
    ], [InlineKeyboardButton("Контакти", callback_data="contact_bot")],[InlineKeyboardButton("Відміна", callback_data="cancel")]])

    return ikb