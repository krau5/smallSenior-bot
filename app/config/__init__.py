from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from dynaconf import Dynaconf


settings: Dynaconf = Dynaconf(
    env='development', # on production change to production
    envvar_prefix='DYNACONF',
    settings_files=['settings.toml', '.secrets.toml'],
)


bot: Bot = Bot(settings.TOKEN)
storage: MemoryStorage = MemoryStorage()
dp: Dispatcher = Dispatcher(bot, storage=storage)
