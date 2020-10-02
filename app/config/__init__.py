from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from dynaconf import Dynaconf


settings = Dynaconf(
    env='development', # on production change to production
    envvar_prefix="DYNACONF",
    settings_files=['settings.toml', '.secrets.toml'],
)


bot = Bot(settings.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
