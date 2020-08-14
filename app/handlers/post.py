from aiogram.types import CallbackQuery
from app.functions.post import count_likes
from app.config import dp, post_calls


async def throttle(*args, **kwargs):
    await args[0].answer("Слишком много запросов")


@dp.callback_query_handler(lambda c: c.data in post_calls)
@dp.throttled(throttle, rate=1)
async def _(c: CallbackQuery):
    await count_likes(c)
