import json
import asyncio
from config_data.config import *
from datetime import datetime
from keyboards.keyboards import *
from aiogram.types import Message


async def get_unexplored_word(chat_id: int):
    '''выдаёт одно слово из списка неизученных'''
    global unexplored_words
    if unexplored_words:
        new_word = unexplored_words.pop(0)
        await bot.send_message(text=f'''❓Как будет <em>"{new_word['на русском']}"</em> на Эсперанто?\n➡️ Ответ: <em><tg-spoiler>{new_word['на эсперанто']}</tg-spoiler></em>\n☝️ Пример предложения: <em><tg-spoiler>{new_word['пример предложения']}</tg-spoiler></em>''',
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


def export_to_unexplored_words(chat_id: int):
    global unexplored_words
    with open(f'users_data/{str(chat_id)}/unexplored_words.json',
              encoding='utf-8', mode='w') as f:
        json.dump(unexplored_words, f, ensure_ascii=False)


