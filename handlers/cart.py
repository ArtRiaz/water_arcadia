from aiogram import types, Dispatcher
from create_bot import dp, bot, support_ids
from aiogram.dispatcher.filters import Text
from aiogram.types.message import ContentType
from aiogram.dispatcher.filters import Command, Text
from data_base.sqlite_db import cb, cur, con
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, LabeledPrice, PreCheckoutQuery, ShippingOption, \
    ShippingQuery

from keyboards.reply import get_back, get_kb_menu
from create_bot import payment_token
from decimal import Decimal



async def empty_cart(message: types.Message):

    user_id = message.chat.id
    cur.execute('DELETE FROM cart WHERE user_id=(?)', (user_id,))
    con.commit()

    await message.answer('Корзина пуста', reply_markup=get_back())


async def add_cart(callback: types.CallbackQuery, callback_data: dict):
    await callback.answer(cache_time=10)
    user_id = callback.message.chat.id
    product_id = callback_data.get('id')
    print(product_id)
    cur.execute('INSERT INTO cart(user_id, product_id) VALUES (?, ?)', (user_id, int(product_id)))
    con.commit()

    await callback.message.answer('Додав!', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Оплатити'), KeyboardButton('Очистити корзину')))


async def send_buy(message: types.Message):
    data = cur.execute('SELECT * FROM cart WHERE user_id=(?)', [message.chat.id]).fetchall()

    new_data = []
    for i in range(len(data)):
        value = cur.execute('SELECT * FROM items WHERE id=(?)', [data[i][2]]).fetchone()
        new_data.append(value)
        print(new_data)

    # new_data = [new_data[i][0] for i in range(len(new_data))]
    # print(new_data)
    prices = [LabeledPrice(label=(i[2] + ' ' + i[3]), amount=i[4] * 100) for i in new_data]

    await bot.send_invoice(message.chat.id,
                           title='Arcadia',
                           description='вода',
                           provider_token=payment_token,
                           currency='UAH',
                           need_phone_number=True,
                           need_shipping_address=True,
                           prices=prices,
                           start_parameter='example',
                           payload='some')


# CITIES_SHIPPING = ShippingOption(
#     id='city',
#     title='Бескоштовна доставка по місту'
# )
#
#
# async def shipping_check(shipping_query: ShippingQuery):
#     shipping_optional = []
#     contries = ['UA']
#
#     if shipping_query.shipping_address.country_code not in contries:
#         return await bot.answer_shipping_query(shipping_query.id, ok=False,
#                                                error_message='У цю страну доставка не можлива')
#     if shipping_query.shipping_address.country_code == 'UA':
#         shipping_optional.append(UA_SHIPPING)
#
#     cities = ['Одеса', 'Одесса', 'Odessa']
#     if shipping_query.shipping_address.city in cities:
#         shipping_optional.append(CITIES_SHIPPING)
#
#     await bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_optional)


async def checkout_procces(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def s_pay(message: types.Message):
    data = cur.execute('SELECT * FROM cart WHERE user_id=(?)', [message.chat.id]).fetchall()

    new_data = []
    for i in range(len(data)):
        value = cur.execute('SELECT * FROM items WHERE id=(?)', [data[i][2]]).fetchall()
        new_data.append(value)
    new_data = [new_data[i][0] for i in range(len(new_data))]
    cur.execute('DELETE FROM cart WHERE user_id=($1)', [message.chat.id]).fetchall()
    con.commit()
    await bot.send_message(chat_id=message.chat.id, text='Оплата пройшла вдало!', reply_markup=get_kb_menu())

    prices = [i[2] + ' ' + i[3] for i in new_data]
    order = (' '.join(map(str, prices)))
    for admin in support_ids:
        await bot.send_message(chat_id=admin,
                               text=f'Інформація про замовлення :\n'
                                    f'Товар: {order}\n'
                                    f'Номер телофону: {message.successful_payment.order_info.phone_number}\n'
                                    f'Адреса: {message.successful_payment.order_info.shipping_address.city}, {message.successful_payment.order_info.shipping_address.street_line1}\n'
                                    f'Сума: {message.successful_payment.total_amount / 100} грн')


def cart(dp: Dispatcher):
    dp.register_callback_query_handler(add_cart, cb.filter(type="buy"))
    dp.register_message_handler(empty_cart, Text(equals='Очистити корзину'))
    dp.register_message_handler(send_buy, Text(equals='Оплатити'))
    dp.register_pre_checkout_query_handler(checkout_procces, lambda q: True)
    dp.register_message_handler(s_pay, content_types=ContentType.SUCCESSFUL_PAYMENT)
#   dp.register_shipping_query_handler(shipping_check)
