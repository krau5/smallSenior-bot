from aiogram.types import Message
# from aiogram.dispatcher import FSMContext

from functions.stats import count_members
from config import dp


@dp.message_handler(commands=['stats'], state="*")
async def stats(message: Message):
    message.answer(count_members())
