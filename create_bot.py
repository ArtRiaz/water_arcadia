from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

support_ids = [
    1064938479
]
token_api = "6330710720:AAG02kfHuDDRcSS2Oh_yfgZthZDx_YfZeR4"
payment_token = "1877036958:TEST:75a5a27101132e13ed1bb842e53596045b37d9a3"

storage = MemoryStorage()
bot = Bot(token_api, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
