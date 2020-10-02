from typing import NoReturn

from aiogram.types import CallbackQuery, Message

from app.config import bot, dp, settings
from app.keyboard.post import create_post_kb
from app.functions.post import count_likes
from app.db.manage_post import insert_post


async def throttle(*args, **kwargs) -> NoReturn:
    await args[0].answer('Слишком много запросов')


@dp.callback_query_handler(lambda c: c.data in settings.post_calls)
@dp.throttled(throttle, rate=1)
async def _(callback: CallbackQuery) -> NoReturn:
    await count_likes(callback)


@dp.channel_post_handler(content_types=['text', 'photo'], state='*')
async def _(message: Message) -> NoReturn:
    message_id: int = message.message_id
    await bot.edit_message_reply_markup(
        settings.channelID, message_id, reply_markup=create_post_kb()
    )
    await insert_post()
    await bot.pin_chat_message(settings.channelID, message_id)
    await bot.delete_message(settings.channelID, message_id + 1)
