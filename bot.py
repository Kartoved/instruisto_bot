'''исполняемый файл'''

import asyncio
import json
from aiogram import Dispatcher
from config_data.config import bot
from handlers import user_handlers
from lexicon import callbacks
from keyboards.set_menu import set_main_menu
from services.services import create_admin_files, check_users_which_should_be_notified


async def main():
    with open("users_data/user_list.json") as f:
        user_list = json.load(f)
    dp: Dispatcher = Dispatcher()
    await bot.delete_my_commands()
    dp.startup.register(set_main_menu)
    dp.include_router(user_handlers.router)
    dp.include_router(callbacks.router)
    create_admin_files()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await check_users_which_should_be_notified(user_list)

if __name__ == '__main__':
    asyncio.run(main())
