from aiogram import Bot, Dispatcher
from environs import Env
from aiogram.contrib.fsm_storage.memory import MemoryStorage


env = Env()
env.read_env()

support_ids = [
    1064938479
]
token_api = env.str("TOKEN_API")
db_user = env.str("USER_DB")
db_pass = env.str("PASS_DB")
payment_token = env.str("PAYMENT_TOKEN")


storage = MemoryStorage()
bot = Bot(token_api, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)