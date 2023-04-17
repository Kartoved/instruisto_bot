import json
import asyncio
from config_data.config import *
from datetime import datetime
from keyboards.keyboards import *


# def change_date(date, value: int) -> str:
#     """меняет дату повторения слова"""
#     date = datetime.strptime(date, '%d-%m-%Y')
#     next_repeat = date + datetime.timedelta(days=value)
#     return next_repeat.strftime('%d-%m-%Y')


# def change_repetition_date(word: dict, value: int):
#     """меняет дату повторения слова"""
#     if value <= 0:
#         value = 0
#         word['дата повторения'] = change_date(word['дата повторения'], 1)
#     elif value == 1:
#         word['дата повторения'] = change_date(word['дата повторения'], 2)
#     elif value == 2:
#         word['дата повторения'] = change_date(word['дата повторения'], 7)
#     elif value == 3:
#         word['дата повторения'] = change_date(word['дата повторения'], 14)
#     elif value == 4:
#         word['дата повторения'] = change_date(word['дата повторения'], 28)
#     elif value == 5:
#         word['дата повторения'] = change_date(word['дата повторения'], 84)
#     elif value == 6:
#         word['дата повторения'] = change_date(word['дата повторения'], 168)
#     return word['дата повторения']


async def get_unexplored_word(chat_id: int):
    '''выдаёт одно слово из списка неизученных'''
    with open(f'users_data/{str(chat_id)}/unexplored_words.json',
              encoding='utf-8') as file:
        unexplored_words = json.load(file)
    if unexplored_words:
        new_word = unexplored_words.pop(0)
        await bot.send_message(text=f'''❓Как будет <em>"{new_word['на русском']}"</em> на Эсперанто?\n➡️ Ответ: <em><tg-spoiler>{new_word['на эсперанто']}</tg-spoiler></em>\n☝️ Пример предложения: <em><tg-spoiler>{new_word['пример предложения']}</tg-spoiler></em>''',
                               chat_id=chat_id,
                               reply_markup=keyboard_add_word)
    else:
        await bot.send_message(text='Все слова изучены. Новых слов нет',
                               chat_id=chat_id)



