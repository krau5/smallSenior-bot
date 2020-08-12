from keyboard.post import create_post_kb
from config import bot, channelID
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db.manage_post import insert_post


async def create_post(state):
    info = await state.get_data()
    res = await bot.send_photo(
        channelID,
        photo=open(info['image_path'], 'rb'),
        caption=info['text'],
        reply_markup=create_post_kb()
    )
    await insert_post(res.message_id)


async def count_likes(call):
    # keyboard = call.message.reply_markup
    [like_text, like] = call.message.reply_markup.inline_keyboard[0][0].text.split()  # noqa: E501
    [dlike_text, dlike] = call.message.reply_markup.inline_keyboard[0][1].text.split()  # noqa: E501

    like = int(like)
    dlike = int(dlike)

    if call.data == "like":
        like_text += f" {like+1}"
        if dlike != 0:
            dlike -= 1
        dlike_text += f" {dlike}"
        keyboard = InlineKeyboardMarkup()
        keyboard.add(
            InlineKeyboardButton(text=like_text, callback_data="like"),
            InlineKeyboardButton(text=dlike_text, callback_data="dlike")
        )
        await bot.edit_message_reply_markup(
            call.message.chat.id,
            call.message.message_id,
            reply_markup=keyboard
        )
