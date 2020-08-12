from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State
from aiogram import Bot, Dispatcher
import json


def read_config():
    with open('config/configuration.json', 'r') as f_obj:
        content = json.load(f_obj)
    return content


config = read_config()

token = config['token']

adminID = config['adminID']
channelID = config['channelID']
chatID = config['chatID']
colors = config['colors']
cluster = config['cluster']

text = State()
image_path = State()

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
