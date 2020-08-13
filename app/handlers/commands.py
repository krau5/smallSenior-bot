# from aiogram.types import Message
# from config import dp, adminID, chatID, channelID
# from functions.stats import count_members
# from keyboard.posts import choose_screen_color


# @dp.message_handler()
# async def commands(message: Message):
#     if (message.from_user.id == adminID):
#         if (message.text == "!channel_stats"):
#             text = await count_members(channelID)
#             await message.answer(text)
#         elif (message.text == "!chat_stats"):
#             text = await count_members(chatID)
#             await message.answer(text)
#         elif (message.text == "!create_post"):
#         await message.answer("Колір:", reply_markup=choose_screen_color())
