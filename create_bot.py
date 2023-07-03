from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN_API = '6032052737:AAEvCcEFhGRajCT0HKwgcwzai1ARjhdMnJs'
PAYMENT_TOKEN = '1877036958:TEST:cfbdda95a4e6c1855d7cd6acde7f5487bfd175ff'
storage = MemoryStorage()
bot = Bot(TOKEN_API, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)

support_ids = [
    1064938479
]
