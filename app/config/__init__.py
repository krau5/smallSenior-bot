from aiogram import Bot, Dispatcher
import json


def readConfig():
    with open('config/configuration.json', 'r') as f_obj:
        content = json.load(f_obj)
    return content


config = readConfig()
token = config['token']

bot = Bot(token)
dp = Dispatcher(bot)
