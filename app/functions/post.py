from typing import NoReturn, Dict, Optional

from aiogram.utils.exceptions import MessageNotModified
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from app.config import bot, settings
from app.keyboard.post import create_post_kb

from app.db.manage_likes import get_likes, update_likes, calc_likes
from app.db.manage_marks import add_mark
from app.db.manage_id import check_id
from app.db.manage_post import insert_post


async def create_post(state: FSMContext) -> NoReturn:
    info: dict = await state.get_data()
    res: Message = await bot.send_photo(
        chat_id=settings.channelID,
        photo=open(info['image_path'], 'rb'),
        caption=info['text'],
        reply_markup=create_post_kb()
    )
    chat_id: int = res.chat.id
    message_id: int = res.message_id

    await bot.pin_chat_message(
        chat_id=chat_id,
        message_id=message_id
    )
    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id + 1
    )
    await insert_post(post_id=message_id)


async def count_likes(callback: CallbackQuery) -> NoReturn:
    message_id: int = callback.message.message_id
    likes_info: Dict[str, int] = await get_likes(post_id=message_id)

    likes: int = likes_info['likes']
    dislikes: int = likes_info['dislikes']

    prev_mark: Optional[bool] = await check_id(
        user_id=callback.from_user.id, post_id=message_id
    )
    await add_mark(callback=callback, prev_mark=prev_mark,
                   curr_mark=callback.data)

    likes, dislikes = await calc_likes(
        callback=callback, prev_mark=prev_mark,
        likes=likes, dislikes=dislikes
    )

    await update_likes(
        post_id=message_id,
        likes=likes,
        dislikes=dislikes
    )

    like_text: str = f'🔥 {likes}'
    dislikes_text: str = f'👎 {dislikes}'

    try:
        await bot.edit_message_reply_markup(
            chat_id=callback.message.chat.id,
            message_id=message_id,
            reply_markup=create_post_kb(
                like_text=like_text,
                dislike_text=dislikes_text
            )
        )
    except MessageNotModified:
        pass
