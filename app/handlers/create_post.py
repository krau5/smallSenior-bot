from aiogram.types import CallbackQuery, Message
from config import bot, dp, colors, text, image_path
from aiogram.dispatcher import FSMContext
from keyboard.post import choose_screen_color_kb
from functions.post import create_post
import datetime


@dp.message_handler(commands='cp')
async def cmd_start(message: Message):
    await text.set()  # set state
    await message.reply("Введи текст нового посту")


@dp.message_handler(state=text)
async def get_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("color:", reply_markup=choose_screen_color_kb())


@dp.callback_query_handler(lambda c: c.data in colors, state=image_path)
async def _(c: CallbackQuery, state: FSMContext):
    await image_path.set()
    today = datetime.datetime.now().strftime("%A")
    path = f'images/{c.data}/{today.lower()}.jpg'
    await state.update_data(image_path=path)
    await bot.delete_message(c.message.chat.id, c.message.message_id)
    await create_post(state)
