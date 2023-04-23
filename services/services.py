import json
import asyncio
from config_data.config import *
import datetime
from keyboards.keyboards import *
from aiogram.types import Message
from lexicon.lexicon import format_learning_message


async def get_unexplored_word(chat_id: int):
    '''выдаёт одно слово из списка неизученных'''
    global unexplored_words
    if unexplored_words:
        new_word = unexplored_words.pop(0)
        await bot.send_message(text=format_learning_message(new_word=new_word),
                               chat_id=chat_id,
                               reply_markup=keyboard_add_word)
    else:
        await bot.send_message(text='Все слова изучены. Новых слов нет',
                               chat_id=chat_id)
    return new_word




def change_date(date: datetime, value: int) -> datetime:
    '''меняет дату повторения слова'''
    date = datetime.datetime.strptime(date, '%d-%m-%Y')
    next_week = date + datetime.timedelta(days=value)
    return next_week.strftime('%d-%m-%Y')
        

def check_coefficient(word: dict, value: int) -> dict:
    '''проверяет текущий коэффициент и изменяет его'''
    if value <= 0:
        word['дата повторения'] = datetime.datetime.now().strftime('%d-%m-%Y')
        word['дата повторения'] = change_date(word['дата повторения'], 1)
    elif value == 1:
        word['дата повторения'] = change_date(word['дата повторения'], 2)
    elif value == 2:
        word['дата повторения'] = change_date(word['дата повторения'], 7)
    elif value == 3:
        word['дата повторения'] = change_date(word['дата повторения'], 14)
    elif value == 4:
        word['дата повторения'] = change_date(word['дата повторения'], 28)
    elif value == 5:
        word['дата повторения'] = change_date(word['дата повторения'], 84)
    elif value == 6:
        word['дата повторения'] = change_date(word['дата повторения'], 168)
    return word










def import_unexplored_words(chat_id: int) -> list:
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


def import_explored_words(chat_id: int) -> list:
    global explored_words
    with open(f'users_data/{str(chat_id)}/explored_words.json',
              encoding='utf-8') as file:
        explored_words = json.load(file)
    return explored_words


def export_explored_words(chat_id: int, new_word: dict):
    global explored_words
    if new_word not in explored_words:
        explored_words.append(new_word)
        with open(f'users_data/{str(chat_id)}/explored_words.json',
                encoding='utf-8', mode='w') as f:
            json.dump(explored_words, f, ensure_ascii=False)
