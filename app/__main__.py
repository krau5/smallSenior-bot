from aiogram.utils import executor
from app.config import dp
from app import handlers

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
