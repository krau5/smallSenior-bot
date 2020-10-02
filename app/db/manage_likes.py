from typing import Dict, Optional, Tuple, NoReturn

from aiogram.types import CallbackQuery

from .main import coll_posts


async def get_likes(post_id: int) -> Dict[str, int]:
    return coll_posts.find_one({'post_id': post_id})


async def update_likes(post_id: int, likes: int, dislikes: int) -> NoReturn:
    coll_posts.update_one(
        {'post_id': post_id},
        {'$set': {
            'likes': likes,
            'dislikes': dislikes
        }}
    )


async def calc_likes(callback: CallbackQuery, prev_mark: Optional[bool],
                     likes: int, dislikes: int) -> Tuple[int, int]:
    if prev_mark is None:  # no mark
        if callback.data == 'likes':
            likes += 1
        elif callback.data == 'dislikes':
            dislikes += 1
    elif not prev_mark:  # previous == dislikes
        if callback.data == 'likes':
            likes += 1
        if dislikes != 0:
            dislikes -= 1
    elif prev_mark:  # previous == likes
        if likes != 0:
            likes -= 1
        if callback.data == 'dislikes':
            dislikes += 1
    return likes, dislikes
