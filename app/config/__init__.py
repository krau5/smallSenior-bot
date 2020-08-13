from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State
from aiogram import Bot, Dispatcher
import yaml


def read_config():
    with open('config/configuration.yaml', 'r') as f_obj:
        content = yaml.load(f_obj, Loader=yaml.FullLoader)
    return content


config = read_config()

token = config['token']
adminID = config['adminID']
channelID = config['channelID']
chatID = config['chatID']
colors = config['colors']
cluster = config['cluster']
post_calls = config['post_calls']

text = State()
image_path = State()

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
