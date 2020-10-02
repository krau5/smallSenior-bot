from datetime import datetime
from typing import NoReturn

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from app.config import bot, dp, settings
from app.functions.post import create_post
from app.keyboard.post import choose_screen_color_kb


class Post(StatesGroup):
    text: State = State()
    image_path: State = State()


@dp.message_handler(commands='cp', state='*')
async def _(message: Message) -> NoReturn:
    if message.from_user.id == settings.adminID:
        await Post.text.set()
        await message.reply('Уведи текст нового посту')


@dp.message_handler(state=Post.text)
async def _(message: Message, state: FSMContext) -> NoReturn:
    await state.update_data(text=message.text)
    await message.answer(text='color:', reply_markup=choose_screen_color_kb())
    await Post.image_path.set()


@dp.callback_query_handler(lambda c: c.data in settings.colors,
                           state=Post.image_path)
async def _(callback: CallbackQuery, state: FSMContext) -> NoReturn:
    today: str = datetime.now().strftime('%A').lower()
    path: str = f'app/images/{callback.data}/{today}.jpg'
    await state.update_data(image_path=path)
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id
    )
    await create_post(state)
