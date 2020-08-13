from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import bot, channelID
from keyboard.post import create_post_kb
from db.manage_post import (
    insert_post, check_id, add_mark, get_likes, update_likes
)


async def create_post(state):
    info = await state.get_data()
    res = await bot.send_photo(
        channelID,
        photo=open(info['image_path'], 'rb'),
        caption=info['text'],
        reply_markup=create_post_kb()
    )
    await insert_post(res.message_id)


async def count_likes(c):
    like = await get_likes(c.message.message_id)
    dlike = await get_likes(c.message.message_id)

    like = int(like[0])
    dlike = int(dlike[1])

    prev_mark = await check_id(c.from_user.id, c.message.message_id)
    await add_mark(c, prev_mark, c.data)

    if prev_mark is None:  # no mark
        if c.data == "likes":
            like += 1
        else:
            dlike += 1
    elif not prev_mark:  # previous == dislike
        if c.data == "likes":
            like += 1
            if dlike != 0:
                dlike -= 1
        else:
            if dlike != 0:
                dlike -= 1
    else:  # previous == like
        if c.data == "likes":
            if like != 0:
                like -= 1
        else:
            if like != 0:
                like -= 1
            dlike += 1

    await update_likes(c.message.message_id, like, dlike)

    like_text = f"🔥 {like}"
    dlike_text = f"👎 {dlike}"

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text=like_text, callback_data="likes"),
        InlineKeyboardButton(text=dlike_text, callback_data="dlikes")
    )

    try:
        await bot.edit_message_reply_markup(
            c.message.chat.id,
            c.message.message_id,
            reply_markup=keyboard
        )
    except Exception:
        pass
