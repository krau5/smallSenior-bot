from aiogram.types import CallbackQuery
from functions.post import count_likes
from config import dp, post_calls


async def hello_throttled(*args, **kwargs):
    call = args[0]
    await call.answer("Слишком много запросов")


@dp.callback_query_handler(lambda c: c.data in post_calls)
@dp.throttled(hello_throttled, rate=2)
async def _(c: CallbackQuery):
    await count_likes(c)
