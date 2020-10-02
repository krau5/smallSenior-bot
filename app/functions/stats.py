from app.config import bot, settings


async def count_members_text(channel_members, chat_members):
    return f"Кількість користувачів у каналі: {channel_members}\n" \
           f"Кількість користувачів у чаті: {chat_members}"


async def count_members():
    channel_members = await bot.get_chat_members_count(
        chat_id=settings.channelID
    )
    chat_members = await bot.get_chat_members_count(
        chat_id=settings.chatID
    )
    text = await count_members_text(channel_members, chat_members)
    return text
