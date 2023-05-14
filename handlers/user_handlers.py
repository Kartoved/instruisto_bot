import hashlib
import json
from os import makedirs, rename, path
from shutil import copy
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from lexicon.lexicon import HELP_COMMAND, CONTACT
from keyboards.keyboards import keybord_start
from lexicon.callbacks import *
from services.services import *


router: Router = Router()


@router.message(Command(commands=['start']))
async def process_start_command(message: Message):
    '''запуск бота, создание необходимых файлов'''
    data = str(message.chat.id).encode() + SALT.encode()
    hashed_id = hashlib.sha256(data).hexdigest()
    if not path.exists(f'users_data/{hashed_id}'):
        makedirs(f'users_data/{hashed_id}', exist_ok=True)
        copy('dictionary.json', f'users_data/{hashed_id}')
        rename(f'users_data/{hashed_id}/dictionary.json',
               f'users_data/{hashed_id}/unexplored_words.json')
        with open(f'users_data/{hashed_id}/explored_words.json',
                  mode='w',
                  encoding='utf-8') as f:
            json.dump([], f)
    else:
        await process_help_command(message)


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    '''вывод приветствия и справки'''
    await message.answer(text=HELP_COMMAND,
                         reply_markup=keybord_start)


@router.message(Command(commands='learning'))
async def start_learning(message: Message):
    '''начать учить неизученные слова'''
    chat_id = message.chat.id
    data = str(message.chat.id).encode() + SALT.encode()
    hashed_id = hashlib.sha256(data).hexdigest()
    explored_words = import_words(hashed_id, 'explored_words')
    unexplored_words = import_words(hashed_id, 'unexplored_words')
    new_word = await get_unexplored_word(chat_id, unexplored_words)
    if new_word:
        new_word = check_and_change_coefficient(
            new_word, new_word['коэффициент'])
        export_words(hashed_id, unexplored_words, 'unexplored_words')
        if new_word not in explored_words:
            explored_words.append(new_word)
            export_words(hashed_id, explored_words, 'explored_words')


@router.message(Command(commands='repeating'))
async def start_repeating(message: Message):
    '''повторение изученных слов'''
    chat_id = message.chat.id
    data = str(message.chat.id).encode() + SALT.encode()
    hashed_id = hashlib.sha256(data).hexdigest()
    explored_words = import_words(hashed_id, 'explored_words')
    await send_explored_word(chat_id, explored_words)
