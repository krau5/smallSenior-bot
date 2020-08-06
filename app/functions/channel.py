from config import bot


async def channel_members_count():
    count = await bot.get_chat_members_count(chat_id="-1001419360985")
    return f'Кол-во пользователей в канале Small Senior: {count}'
