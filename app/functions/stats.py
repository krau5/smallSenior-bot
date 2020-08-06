from config import bot, chatID


async def count_members(id):
    count = await bot.get_chat_members_count(chat_id=id)
    if (id == chatID):
        return f'Кол-во пользователей в чате Small Senior: {count}'
    else:
        return f'Кол-во пользователей в канале Small Senior: {count}'
