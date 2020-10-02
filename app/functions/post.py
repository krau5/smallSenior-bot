from aiogram.utils.exceptions import MessageNotModified

from app.config import bot, settings
from app.keyboard.post import create_post_kb

from app.db.manage_likes import get_likes, update_likes, calc_likes
from app.db.manage_marks import add_mark
from app.db.manage_id import check_id
from app.db.manage_post import insert_post


async def create_post(state):
    info = await state.get_data()
    res = await bot.send_photo(
        settings.channelID,
        photo=open(info['image_path'], 'rb'),
        caption=info['text'],
        reply_markup=create_post_kb()
    )
    await bot.pin_chat_message(res.chat.id, res.message_id)
    await bot.delete_message(res.chat.id, res.message_id+1)
    await insert_post(res.message_id)


async def count_likes(c):
    likes_info = await get_likes(c.message.message_id)

    like = int(likes_info[0])
    dlike = int(likes_info[1])

    prev_mark = await check_id(c.from_user.id, c.message.message_id)
    await add_mark(c, prev_mark, c.data)

    [like, dlike] = await calc_likes(c, prev_mark, like, dlike)

    await update_likes(c.message.message_id, like, dlike)

    like_text = f"🔥 {like}"
    dlike_text = f"👎 {dlike}"

    try:
        await bot.edit_message_reply_markup(
            c.message.chat.id,
            c.message.message_id,
            reply_markup=create_post_kb(like_text, dlike_text)
        )
    except MessageNotModified:
        pass
