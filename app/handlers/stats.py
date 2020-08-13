from aiogram.types import Message

from functions.stats import count_members
from config import dp


@dp.message_handler(commands=['stats'], state="*")
async def stats(message: Message):
    await message.answer(await count_members())
