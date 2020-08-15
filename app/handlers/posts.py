from aiogram.types import CallbackQuery

from app.config import bot, dp, post_calls, channelID
from app.keyboard.post import create_post_kb
from app.functions.post import count_likes
from app.db.manage_post import insert_post


async def throttle(*args, **kwargs):
    await args[0].answer("Слишком много запросов")


@dp.callback_query_handler(lambda c: c.data in post_calls)
@dp.throttled(throttle, rate=1)
async def _(c: CallbackQuery):
    await count_likes(c)


@dp.channel_post_handler(content_types=['text', 'photo'], state="*")
async def _(message):
    await bot.edit_message_reply_markup(
        channelID, message.message_id, reply_markup=create_post_kb()
    )
    await insert_post(message.message_id)
    await bot.pin_chat_message(channelID, message.message_id)
    await bot.delete_message(channelID, message.message_id+1)
