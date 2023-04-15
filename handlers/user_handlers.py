from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from lexicon.lexicon import HELP_COMMAND
from keyboards.keyboards import keyboard_contact

router: Router = Router()


@router.message(Command(commands=['start', 'help']))
async def process_start_command(message: Message):
    '''вывод приветствия и справки'''
    await message.answer(text=HELP_COMMAND)


@router.message(Command(commands=['contact']))
async def contact_with_developer(message: Message):
    '''Выводит контакты разработчика'''
    await message.answer(text='Пиши мне про баги и слова благодарности 🥳',
                         reply_markup=keyboard_contact)
