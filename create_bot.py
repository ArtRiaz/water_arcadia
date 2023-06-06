from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage


TOKEN_API='6227999079:AAHY02ob6FsawNfOJY-A0ZfLy-HHgqF4ujk'
storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=storage)

support_ids = [
    1064938479
]