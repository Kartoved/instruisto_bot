import json
import asyncio
from config_data.config import *
from datetime import datetime
from keyboards.keyboards import *
from aiogram.types import Message
from lexicon.lexicon import format_learning_message


async def get_unexplored_word(chat_id: int):
    '''выдаёт одно слово из списка неизученных'''
    global unexplored_words, explored_words
    if unexplored_words:
        new_word = unexplored_words.pop(0)
        explored_words.append(new_word)
        await bot.send_message(text=format_learning_message(new_word=new_word),
                               chat_id=chat_id,
                               reply_markup=keyboard_add_word)
    else:
        await bot.send_message(text='Все слова изучены. Новых слов нет',
                               chat_id=chat_id)


def import_unexpored_words(chat_id) -> list:
    global unexplored_words
    with open(f'users_data/{str(chat_id)}/unexplored_words.json',
              encoding='utf-8') as file:
        unexplored_words = json.load(file)
    return unexplored_words


def export_unexplored_words(chat_id: int):
    global unexplored_words
    with open(f'users_data/{str(chat_id)}/unexplored_words.json',
              encoding='utf-8', mode='w') as f:
        json.dump(unexplored_words, f, ensure_ascii=False)


def import_explored_words(chat_id) -> list:
    global explored_words
    with open(f'users_data/{str(chat_id)}/explored_words.json',
              encoding='utf-8') as file:
        explored_words = json.load(file)
    return explored_words


def export_explored_words(chat_id: int):
    global explored_words
    with open(f'users_data/{str(chat_id)}/explored_words.json',
              encoding='utf-8', mode='w') as f:
        json.dump(explored_words, f, ensure_ascii=False)
