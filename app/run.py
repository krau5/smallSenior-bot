from aiogram.utils import executor
from config import dp
import handlers  # noqa: F401

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
