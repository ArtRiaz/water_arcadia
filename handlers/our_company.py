from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.reply import kb_menu, get_kb_menu,get_back
from aiogram.dispatcher.filters import Text





async def cmd_menu(message: types.Message):
    await message.delete()
    #    await message.answer('Управления меню', reply_markup=get_kb_menu())
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://yandex.by/images/search?img_url=https%3A%2F%2Fsun9-81.userapi.com%2Fimpg'
                               '%2FCOLOTXGpYefkgXG2sLaO4kfkKzCeBDCfhliaRQ%2FkN3LG58SPNo.jpg%3Fsize%3D960x720'
                               '%26quality%3D95%26sign%3De74cffdf9ce01aaf559fe0a22cf12d73%26c_uniq_tag'
                               '%3DeFTmrRuHf7H9ytd67uxVXIisonX-znqS2cjZtq-Z5uc%26type%3Dalbum&lr=87&nomisspell=1'
                               '&ogl_url=https%3A%2F%2Fsun9-81.userapi.com%2Fimpg'
                               '%2FCOLOTXGpYefkgXG2sLaO4kfkKzCeBDCfhliaRQ%2FkN3LG58SPNo.jpg%3Fsize%3D960x720'
                               '%26quality%3D95%26sign%3De74cffdf9ce01aaf559fe0a22cf12d73%26c_uniq_tag'
                               '%3DeFTmrRuHf7H9ytd67uxVXIisonX-znqS2cjZtq-Z5uc%26type%3Dalbum&pos=3&redircnt'
                               '=1685175286.1&rlt_url=http%3A%2F%2F239detsad.ru%2FKartinka%2FMarker_gruppa'
                               '%2Fvolshebnye_kapelki.png&rpt=simage&source=related-5&text=вода%20картинки%20для%20'
                               'детей',
                         caption=f'Вода «Arcadia» завдяки природному походження нашої води, вона не просто смачна '
                                 f'сама по собі, а й дарує незабутній смак усім вашим стравам та напоям.!!!',
                         reply_markup=get_back())


def register_handlers_about(dp: Dispatcher):
    dp.register_message_handler(cmd_menu, Text(equals='Наша компанія'))
