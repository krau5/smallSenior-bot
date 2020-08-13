from config import bot, chatID


async def count_members(_id):
    count = await bot.get_chat_members_count(chat_id=_id)
    if _id == chatID:
        return f'Кол-во пользователей в чате Small Senior: {count}'
    else:
        return f'Кол-во пользователей в канале Small Senior: {count}'
