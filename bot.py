import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import bot, config
from handlers import user_handlers
from lexicon import callbacks
from keyboards.set_menu import set_main_menu


async def main():
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(callbacks.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await set_main_menu(bot)

if __name__ == '__main__':
    asyncio.run(main())
