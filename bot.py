'''исполняемый файл'''

import asyncio
from aiogram import Dispatcher
from config_data.config import bot
from handlers import user_handlers
from callbacks import callbacks
from keyboards.set_menu import set_main_menu
from services.services import create_admin_files, run_scheduler, scheduler


async def main():
    '''точка входа в бота'''
    dp: Dispatcher = Dispatcher()
    dp.startup.register(set_main_menu)
    dp.include_router(user_handlers.router)
    dp.include_router(callbacks.router)
    create_admin_files()
    run_scheduler(scheduler)
    await bot.delete_my_commands()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
