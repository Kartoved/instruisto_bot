'''исполняемый файл'''

import asyncio
import json
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from aiogram import Dispatcher
from config_data.config import bot
from handlers import user_handlers
from lexicon import callbacks
from keyboards.set_menu import set_main_menu
from services.services import create_admin_files


async def main():
    dp: Dispatcher = Dispatcher()
    dp.startup.register(set_main_menu)
    dp.include_router(user_handlers.router)
    dp.include_router(callbacks.router)
    create_admin_files()
    scheduler = AsyncIOScheduler()
    with open('users_data/reminders.json', 'r', encoding='utf-8') as f:
        reminders = json.load(f)
    for chat_id, value in reminders.items():
        scheduler.add_job(user_handlers.send_message_cron,
                          trigger='cron',
                          hour=value[0:2],
                          minute=value[3:5],
                          kwargs={'bot': bot, 'chat_id': chat_id})
    scheduler.start()
    await bot.delete_my_commands()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
