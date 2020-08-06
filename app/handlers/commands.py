from aiogram.types import Message
from config import dp, adminID
from functions.channel import channel_members_count


@dp.message_handler()
async def commands(message: Message):
    if (message.from_user.id == adminID):
        if (message.text == "!channelStats"):
            text = await channel_members_count()
            await message.answer(text)
