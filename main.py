import asyncio
import logging
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from datetime import datetime as date
from config import log_file_path, DEBUG_MODE

from handlers import bot, router, db_connect_thread


async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router=router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


def log_file_create() -> str:
    date_now = date.now()
    filename = log_file_path + date_now.strftime("%d_%m_%Y#%H-%M-%S") + ".log"

    with open(filename, "w") as file:
        pass

    return filename


if __name__ == "__main__":
    if DEBUG_MODE:
        logging.basicConfig(level=logging.DEBUG)
    else:
        log_file_name = log_file_create()
        logging.basicConfig(filename=log_file_name, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    asyncio.run(main())
    db_connect_thread.close()
