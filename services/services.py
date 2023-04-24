import json
import asyncio
from config_data.config import *
from datetime import datetime, timedelta
from keyboards.keyboards import *
from lexicon.lexicon import format_learning_message, format_repeating_message


async def get_unexplored_word(chat_id: int) -> dict:
    '''выдаёт одно слово из списка неизученных'''
    global unexplored_words
    if unexplored_words:
        new_word = unexplored_words.pop(0)
        await bot.send_message(text=format_learning_message(new_word),
                               chat_id=chat_id,
                               reply_markup=keyboard_add_word)
    else:
        await bot.send_message(text='Все слова изучены. Новых слов нет.',
                               chat_id=chat_id)
    return new_word


def change_date(value: int) -> str:
    '''меняет дату повторения слова'''
    date = datetime.now()
    date = date + timedelta(days=value)
    return date.strftime('%d-%m-%Y')


def check_and_change_coefficient(word: dict, value: int, remember: bool) -> dict:
    '''проверяет текущий коэффициент и изменяет его'''
    if remember and value < 6:
        value += 1
    elif not remember and value > 0:
        value -= 1
    word['коэффициент'] = value
    if value <= 0:
        word['дата повторения'] = str(change_date(1))
    elif value == 1:
        word['дата повторения'] = str(change_date(2))
    elif value == 2:
        word['дата повторения'] = str(change_date(7))
    elif value == 3:
        word['дата повторения'] = str(change_date(14))
    elif value == 4:
        word['дата повторения'] = str(change_date(28))
    elif value == 5:
        word['дата повторения'] = str(change_date(84))
    elif value == 6:
        word['дата повторения'] = str(change_date(168))
    else:
        word['дата повторения'] = 'str(change_date(168))'
    return word


async def send_explored_word(chat_id: int, explored_words: list) -> dict:
    for word in explored_words:
        if datetime.strptime(word['дата повторения'], "%d-%m-%Y") <= datetime.now():
            return await bot.send_message(text=format_repeating_message(word),
                                          chat_id=chat_id,
                                          reply_markup=keyboard_check_word)
    return await bot.send_message(text='На сегодня слов для повторения нет.',
                                  chat_id=chat_id)


def get_explored_word(explored_words: list) -> dict:
    for word in explored_words:
        if datetime.strptime(word['дата повторения'], "%d-%m-%Y") <= datetime.now():
            return word


def import_unexplored_words(chat_id: int) -> list:
    global unexplored_words
    with open(f'users_data/{str(chat_id)}/unexplored_words.json',
              encoding='utf-8') as file:
        unexplored_words = json.load(file)
    return unexplored_words


def import_explored_words(chat_id: int) -> list:
    global explored_words
    with open(f'users_data/{str(chat_id)}/explored_words.json',
              encoding='utf-8') as file:
        explored_words = json.load(file)
    return explored_words


def export_unexplored_words(chat_id: int):
    global unexplored_words
    with open(f'users_data/{str(chat_id)}/unexplored_words.json',
              encoding='utf-8', mode='w') as f:
        json.dump(unexplored_words, f, ensure_ascii=False)


def export_explored_words(chat_id: int, new_word: dict):
    global explored_words
    if new_word not in explored_words:
        explored_words.append(new_word)
        with open(f'users_data/{str(chat_id)}/explored_words.json',
                  encoding='utf-8', mode='w') as f:
            json.dump(explored_words, f, ensure_ascii=False)
