from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from lexicon.lexicon import HELP_COMMAND, get_profile_message
from keyboards.keyboards import keybord_start, keyboard_profile
from lexicon.callbacks import *
from services.services import *


router: Router = Router()


@router.message(Command(commands=['start']))
async def process_start_command(message: Message):
    '''запуск бота, создание необходимых файлов'''
    chat_id = message.chat.id
    create_user_folders(chat_id)
    add_user_to_list(chat_id)
    await process_help_command(message)


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    '''вывод приветствия и справки'''
    await message.answer(text=HELP_COMMAND,
                         reply_markup=keybord_start)


@router.message(Command(commands=['stop', 'profile']))
async def show_profile(message: Message):
    chat_id = message.chat.id
    explored_words = import_words(chat_id, 'explored_words')
    text = get_profile_message(message.from_user.username, explored_words)
    await bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard_profile)


@router.message(Command(commands='learning'))
async def start_learning(message: Message):
    '''начать учить неизученные слова'''
    chat_id = message.chat.id
    explored_words = import_words(chat_id, 'explored_words')
    unexplored_words = import_words(chat_id, 'unexplored_words')
    new_word = await get_unexplored_word(chat_id, unexplored_words)
    if new_word:
        new_word = check_and_change_coefficient(
            new_word, new_word['коэффициент'])
        export_words(chat_id, unexplored_words, 'unexplored_words')
        if new_word not in explored_words:
            explored_words.append(new_word)
            export_words(chat_id, explored_words, 'explored_words')


@router.message(Command(commands='repeating'))
async def start_repeating(message: Message):
    '''повторение изученных слов'''
    chat_id = message.chat.id
    explored_words = import_words(chat_id, 'explored_words')
    await send_explored_word(chat_id, explored_words)
