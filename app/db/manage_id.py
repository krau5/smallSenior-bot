from typing import NoReturn, Optional

from aiogram.types import CallbackQuery

from .main import coll_posts


async def pull_id(callback: CallbackQuery, mark_type: str) -> NoReturn:
    coll_posts.update_one(
        {'post_id': callback.message.message_id},
        {'$pull':  {f'marks.{mark_type}': callback.from_user.id}}
    )


async def push_id(callback: CallbackQuery, mark_type: str) -> NoReturn:
    coll_posts.update_one(
        {'post_id': callback.message.message_id},
        {'$addToSet':  {f'marks.{mark_type}': callback.from_user.id}}
    )


async def check_id(user_id, post_id) -> Optional[bool]:
    found_post: dict = coll_posts.find_one({
        'post_id': post_id
    }, {'_id': 0})

    likes: int = found_post['marks']['likes']
    dislikes: int = found_post['marks']['dislikes']

    if user_id not in (*likes, *dislikes):
        return
    if user_id in likes:
        return True
    return False
