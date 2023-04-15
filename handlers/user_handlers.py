import json
from os import makedirs, rename, path
from shutil import copy
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from lexicon.lexicon import HELP_COMMAND
from keyboards.keyboards import keyboard_contact

router: Router = Router()

@router.message(Command(commands=['start']))
async def process_start_command(message: Message):
    '''запуск бота, создание необходимых файлов'''
    if not path.exists(f'users_data/{str(message.chat.id)}'):
        makedirs(f'users_data/{str(message.chat.id)}', exist_ok=True)
        copy('dictionary.json', f'users_data/{str(message.chat.id)}')
        rename(f'users_data/{str(message.chat.id)}/dictionary.json',
            f'users_data/{str(message.chat.id)}/unexplorer_words.json')
        with open(f'users_data/{str(message.chat.id)}/unexplorer_words.json',
                encoding='utf-8') as f:
            unstudied_list = json.load(f)
        with open(f'users_data/{str(message.chat.id)}/explorer_words.json',
                mode='w',
                encoding='utf-8') as f:
            json.dump([], f)

@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    '''вывод приветствия и справки'''
    await message.answer(text=HELP_COMMAND)


@router.message(Command(commands=['contact']))
async def contact_with_developer(message: Message):
    '''Выводит контакты разработчика'''
    await message.answer(text='Пиши мне про баги и слова благодарности 🥳',
                         reply_markup=keyboard_contact)
