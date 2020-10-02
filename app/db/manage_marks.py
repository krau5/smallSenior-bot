from typing import NoReturn, Optional

from aiogram.types import CallbackQuery

from .manage_id import push_id, pull_id


async def add_mark(callback: CallbackQuery, prev_mark: Optional[bool],
                   curr_mark: str) -> NoReturn:
    if prev_mark is None:  # no previous mark
        await callback.answer(text='Спасибо за оценку')
        await push_id(callback=callback, mark_type=curr_mark)

    if prev_mark and curr_mark == 'likes':
        await callback.answer(text='Оценка снята')
        await pull_id(callback=callback, mark_type='likes')
    elif prev_mark and curr_mark == 'dislikes':  # curr_mark == dislike
        await callback.answer('Спасибо за оценку')
        await pull_id(callback=callback, mark_type='likes')
        await push_id(callback=callback, mark_type=curr_mark)

    elif not prev_mark and curr_mark == 'likes':
        await callback.answer(text='Спасибо за оценку')
        await pull_id(callback=callback, mark_type='dislikes')
        await push_id(callback=callback, mark_type=curr_mark)
    elif not prev_mark and curr_mark == 'dislikes':
        await callback.answer(text="Оценка снята")
        await pull_id(callback=callback, text='dislikes')
