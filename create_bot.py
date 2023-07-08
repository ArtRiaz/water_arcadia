from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN_API = '5849975115:AAGF8AL4QSaRqf2bekYEGmK1-fud-SlXWNc'
PAYMENT_TOKEN = '1877036958:TEST:a0fbd1fd1dda1c7f6df7aebb3ba467a50c0e545e'
DATABASE_URL = "postgres://postgres:2288@localhost:5432/arcadia"

storage = MemoryStorage()
bot = Bot(TOKEN_API, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)

support_ids = [
    1064938479
]
