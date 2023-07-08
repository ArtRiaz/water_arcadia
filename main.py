from aiogram import types, executor
from create_bot import dp, bot
from handlers import start, our_company, contact, inline_menu, back_to_menu, support, question, order, calendar, admin,cart
import logging
from data_base.sqlite_db import sql_start
from utils.set_bot_commands import set_commands


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def on_startup(_):
    await sql_start()
    print('Бот запущен')
    print('База данных запущена')
    await set_commands(bot=bot)


start.register_handlers_start(dp)
our_company.register_handlers_about(dp)
back_to_menu.register_handler_back(dp)
contact.register_handler_contact(dp)
inline_menu.register_inline_menu(dp)
support.get_support(dp)
question.question_menu(dp)
order.handler_order(dp)
calendar.handler_calendar(dp)
admin.register_handlers_start_admin(dp)
cart.cart(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)
