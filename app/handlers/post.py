from aiogram.types import CallbackQuery
from functions.post import count_likes
from config import dp


@dp.callback_query_handler(lambda call: call.data == "like")
async def _(call: CallbackQuery):
    await count_likes(call)
