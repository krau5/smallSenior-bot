from aiogram.types import Message
from config import dp


@dp.message_handler()
async def commands(message: Message):
    await message.answer("Hello, world")
