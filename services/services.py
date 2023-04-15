import json
import asyncio
from config_data.config import *



async def get_one_word(chat_id: int):
    '''выдаёт одно слово из списка неизученных'''
    with open(f'users_data/{str(chat_id)}/unexplorer_words.json',
              encoding='utf-8') as file:
        unexplorer_words = json.load(file)
    if unexplorer_words:
        new_word = unexplorer_words.pop(0)
        print(new_word)
        # list_of_keys = list(new_word)
        await bot.send_message(text=f'''Как будет <strong>"{new_word['на русском']}</strong> на Эсперанто? 
                                Ответ: <b><tg-spoiler>{new_word['на эсперанто']}</tg-spoiler></b> 
                                Пример предложения: <em><tg-spoiler>{new_word['пример предложения']}</tg-spoiler></em>''',
                        chat_id=chat_id)
        # change_repetition_date(new_word, new_word['коэффциет'])
        # add_to_studied(new_word, chat_id=chat_id)
        # delete_from_unstudied(unstudied_list, chat_id)
    else:
        await bot.send_message(text='Все слова изучены. Новых слов нет',
                        chat_id=chat_id)