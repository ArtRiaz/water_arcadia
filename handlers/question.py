from aiogram.types import CallbackQuery
from create_bot import bot, dp
from aiogram import Dispatcher
from keyboards.reply import get_back
from aiogram import types, Dispatcher
from keyboards.inline import ikb_question, ikb_question_order, ikb_question_info, ikb_question_contact, ikb_contact
from aiogram.dispatcher.filters import Text


async def questions(message: types.Message):
    with open('water_start.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id, photo=photo, reply_markup=get_back())
        await message.answer("Відповіді на ваші запитання:", reply_markup=ikb_question())


async def question_1(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Замовлення можно зробити на нашему сайті або на нашому телеграм боті: ",
                                  reply_markup=ikb_question_order())


async def question_2(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Детальну інформацію ми можите знайти на нашому сайті та у розділі Наша компанія: ",
                                  reply_markup=ikb_question_info())


async def question_3(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Умови доставки можно знайти на нашому сайті та у нашому телеграм боті: ",
                                  reply_markup=ikb_question_order())


async def question_4(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Зв'язатись з нами можна через розділ Контакти та наш сайт: ",
                                  reply_markup=ikb_question_contact())


async def inline_cancel(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Відміна", reply_markup=ikb_question())


async def inline_contact(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Як з нами зв'язатись:", reply_markup=ikb_contact())


async def inline_company(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Вода «Arcadia» завдяки природному походження нашої води, вона не просто смачна "
                                  "сама по собі, а й дарує незабутній смак усім вашим стравам та напоям.",
                                  reply_markup=get_back())


def question_menu(dp: Dispatcher):
    dp.register_message_handler(questions, Text(equals="Найчастіщі запитання"))
    dp.register_callback_query_handler(question_1, text='1')
    dp.register_callback_query_handler(question_2, text='2')
    dp.register_callback_query_handler(question_3, text='3')
    dp.register_callback_query_handler(question_4, text='4')
    dp.register_callback_query_handler(inline_cancel, text='cancel')
    dp.register_callback_query_handler(inline_contact, text='contact_bot')
    dp.register_callback_query_handler(inline_company, text='info_bot')
