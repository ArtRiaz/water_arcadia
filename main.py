from aiogram import executor, types
#import db_sqlite
#from db_sqlite import *
from create_bot import dp
#from middleware.support_middleware import SupportMiddleware
from handlers import start, our_company, contact, inline_menu, back_to_menu, support, question, order, calendar
#from aiogram.dispatcher import middlewares
from utils.set_bot_commands import set_default_commands


async def on_startup(_):
#    db_sqlite.sq.connect('database.db')
    await set_default_commands(dp)
    print('Бот запущен')
    print('База данных запущена')


#dp.middleware.setup(SupportMiddleware())

start.register_handlers_start(dp)
our_company.register_handlers_about(dp)
back_to_menu.register_handler_back(dp)
# profiles.register_handler_profiles(dp)
contact.register_handler_contact(dp)
inline_menu.register_inline_menu(dp)
# registration.consultat(dp)
support.get_support(dp)
question.question_menu(dp)
order.handler_order(dp)
calendar.handler_calendar(dp)
#support_call.get_support_call(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)