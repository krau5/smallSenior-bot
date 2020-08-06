from aiogram import Bot, Dispatcher
import json


def read_config():
    with open('config/configuration.json', 'r') as f_obj:
        content = json.load(f_obj)
    return content


config = read_config()

token = config['token']
adminID = config['adminID']

bot = Bot(token)
dp = Dispatcher(bot)
