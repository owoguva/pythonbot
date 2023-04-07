from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config


storage = MemoryStorage()

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMINS = (890463711)
OPENAI_TOKEN = "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"


