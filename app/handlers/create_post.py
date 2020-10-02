import datetime

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from app.config import bot, dp, settings
from app.functions.post import create_post
from app.keyboard.post import choose_screen_color_kb


class Post(StatesGroup):
    text = State()
    image_path = State()


@dp.message_handler(commands="cp", state="*")
async def cmd_start(message: Message):
    if message.from_user.id == settings.adminID:
        await Post.text.set()
        await message.reply("Введи текст нового посту")


@dp.message_handler(state=Post.text)
async def get_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("color:", reply_markup=choose_screen_color_kb())
    await Post.image_path.set()


@dp.callback_query_handler(lambda c: c.data in settings.colors,
                           state=Post.image_path)
async def _(c: CallbackQuery, state: FSMContext):
    today = datetime.datetime.now().strftime("%A")
    path = f'app/images/{c.data}/{today.lower()}.jpg'
    await state.update_data(image_path=path)
    await bot.delete_message(c.message.chat.id, c.message.message_id)
    await create_post(state)
