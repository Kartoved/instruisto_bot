import json
from os import makedirs, rename, path
from shutil import copy
from aiogram.types import Message
from config_data.config import *
from datetime import datetime, timedelta
from keyboards.keyboards import *
from lexicon.lexicon import format_learning_message, format_repeating_message


async def get_unexplored_word(chat_id: int, unexplored_words: list) -> dict:
    '''выдаёт одно слово из списка неизученных'''
    if unexplored_words:
        new_word = unexplored_words.pop(0)
        await bot.send_message(text=format_learning_message(new_word),
                               chat_id=chat_id,
                               reply_markup=keyboard_add_word)
    else:
        new_word = {}
        await bot.send_message(text='Все слова изучены. Новых слов нет.',
                               chat_id=chat_id)
    return new_word


# def highlight_word(word: dict):
#     new_sentence = word['пример предложения'].split(' ')
#     print(word['на эсперанто'][-1])
#     for x in new_sentence:
#         if x == word['на эсперанто']:
#             new_sentence[x] = f'<strong>{x}</strong>'
#     print(new_sentence)


def change_date(value: int) -> str:
    '''меняет дату повторения слова'''
    date = datetime.now()
    date = date + timedelta(days=value)
    return date.strftime('%d-%m-%Y')


def check_and_change_coefficient(word: dict, value: int, remember: bool = False) -> dict:
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
    return word


async def send_explored_word(chat_id: int, explored_words: list) -> dict:
    '''отправить пользователю изученное слово'''
    for word in explored_words:
        if datetime.strptime(word['дата повторения'], "%d-%m-%Y") <= datetime.now():
            # highlight_word(word)
            return await bot.send_message(text=format_repeating_message(word),
                                          chat_id=chat_id,
                                          reply_markup=keyboard_check_word)
    return await bot.send_message(text='На сегодня слов для повторения нет.',
                                  chat_id=chat_id)


def get_explored_word(explored_words: list) -> dict:
    '''получить слово из списка изученных'''
    for word in explored_words:
        if datetime.strptime(word['дата повторения'], "%d-%m-%Y") <= datetime.now():
            return word


def import_words(chat_id: str, list_name: str) -> list:
    '''импортирует список слов в программу'''
    with open(f'users_data/{chat_id}/{list_name}.json',
              encoding='utf-8') as f:
        list_of_words = json.load(f)
    return list_of_words


def export_words(chat_id: str, list_of_words: list, list_name: str):
    '''экспортирует слова в выбранный список слов'''
    with open(f'users_data/{chat_id}/{list_name}.json',
              encoding='utf-8',
              mode='w') as f:
        json.dump(list_of_words, f, ensure_ascii=False)

def create_user_folders(chat_id: int):
    if not path.exists(f'users_data/{chat_id}'):
        makedirs(f'users_data/{chat_id}', exist_ok=True)
        copy('dictionary.json', f'users_data/{chat_id}')
        rename(f'users_data/{chat_id}/dictionary.json',
               f'users_data/{chat_id}/unexplored_words.json')
        with open(f'users_data/{chat_id}/explored_words.json',
                  mode='w', encoding='utf-8') as f:
            json.dump([], f)
    