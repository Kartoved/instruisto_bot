"""необходимые функции"""

import json
from os import makedirs, rename, path
from shutil import copy
from datetime import datetime, timedelta
from config_data.config import bot
from keyboards.keyboards import keyboard_add_word, keyboard_check_word, keyboard_open_profile
from lexicon.lexicon import format_learning_message, format_repeating_message


async def get_unexplored_word(chat_id: int, unexplored_words: list) -> dict:
    """выдаёт одно слово из списка неизученных"""
    if unexplored_words:
        new_word: dict = unexplored_words.pop(0)
        await bot.send_message(text=format_learning_message(new_word),
                               chat_id=chat_id,
                               reply_markup=keyboard_add_word)
    else:
        new_word: dict = {}
        await bot.send_message(text="Все слова изучены. Новых слов нет.",
                               chat_id=chat_id)
    return new_word


def change_date(value: int) -> str:
    """меняет дату повторения слова"""
    date: datetime = datetime.now()
    date = date + timedelta(days=value)
    return date.strftime("%d-%m-%Y")


def check_and_change_coefficient(word: dict,
                                 interval: int,
                                 remember: bool = False) -> dict:
    """проверяет текущий интервал и изменяет его"""
    if remember and interval < 6:
        interval += 1
    elif not remember and interval > 0:
        interval -= 1
    word["интервал"]: int = interval
    interval_to_days = [1, 2, 7, 14, 28, 84, 168]
    word["дата повторения"] = str(change_date(interval_to_days[interval]))
    return word


async def send_explored_word(chat_id: int, explored_words: list) -> dict:
    """отправить пользователю изученное слово"""
    for word in explored_words:
        if datetime.strptime(word["дата повторения"], "%d-%m-%Y") <= datetime.now():
            return await bot.send_message(text=format_repeating_message(word),
                                          chat_id=chat_id,
                                          reply_markup=keyboard_check_word)
    date_of_closest_repetition = get_date_of_closest_repetition(explored_words)
    return await bot.send_message(text=f'📆 На сегодня слов для повторения нет.\n\n\
Ближайшее повторение слов будет <strong> {date_of_closest_repetition}</strong>',
                                  chat_id=chat_id,
                                  reply_markup=keyboard_open_profile)


def get_date_of_closest_repetition(explored_words: list) -> str:
    """получить дату ближайшего повторения"""
    date_of_closest_repetition = datetime.strptime(
        explored_words[0]["дата повторения"], "%d-%m-%Y")
    for word in explored_words:
        if datetime.strptime(word["дата повторения"], "%d-%m-%Y") < date_of_closest_repetition:
            date_of_closest_repetition = datetime.strptime(
                word["дата повторения"], "%d-%m-%Y")
    return date_of_closest_repetition.strftime("%d-%m-%Y")


def get_explored_word(explored_words: list) -> dict:
    """получить слово из списка изученных"""
    for word in explored_words:
        if datetime.strptime(word["дата повторения"], "%d-%m-%Y") <= datetime.now():
            return word


def import_words(chat_id: str, list_name: str) -> list:
    """импортирует список слов в программу"""
    with open(f"users_data/{chat_id}/{list_name}.json", encoding="utf-8") as f:
        list_of_words: list = json.load(f)
    return list_of_words


def export_words(chat_id: str, list_of_words: list, list_name: str):
    """экспортирует слова в выбранный список слов"""
    with open(
        f"users_data/{chat_id}/{list_name}.json", encoding="utf-8", mode="w"
    ) as f:
        json.dump(list_of_words, f, ensure_ascii=False)


def create_admin_files():
    """создает файлы для админа"""
    makedirs("users_data", exist_ok=True)
    makedirs("reports", exist_ok=True)
    with open("reports/reports_statements.json", "w") as reports:
        json.dump({}, reports)


def create_user_folders(chat_id: int):
    """создаёт папку пользователя"""
    if not path.exists(f"users_data/{chat_id}"):
        makedirs(f"users_data/{chat_id}", exist_ok=True)
        copy("services/dictionary.json", f"users_data/{chat_id}")
        rename(f"users_data/{chat_id}/dictionary.json",
               f"users_data/{chat_id}/unexplored_words.json")
        with open(f"users_data/{chat_id}/explored_words.json",
                  mode="w",
                  encoding="utf-8") as f:
            json.dump([], f)


def add_user_to_list(chat_id):
    """добавляет юзера в список юзеров"""
    try:
        with open("users_data/user_list.json") as f:
            user_list: list = json.load(f)
            if chat_id not in user_list:
                user_list.append(chat_id)
                with open("users_data/user_list.json", "w") as f:
                    json.dump(user_list, f)
    except FileNotFoundError:
        with open("users_data/user_list.json", "w") as f:
            user_list: list = [chat_id]
            json.dump(user_list, f)


def export_report(chat_id: int, report: str, username: str):
    """экспортирует багрепорт в файл"""
    date = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    with open(f"reports/{date}.txt", "w", encoding="utf-8") as f:
        f.write(f'from user: {username}\n\n"{report}"')


def send_reminder(chat_id):
    """отправляет напоминание о повторении слов в нужный день"""
    list_of_words = import_words(chat_id, "explored_words")
    text = f'Привет! Сегодня есть слова для повторения! Давай заниматься!'
    for word in list_of_words:
        if datetime.strptime(word["дата повторения"], "%d-%m-%Y") <= datetime.now().strftime("%d-%m-%Y"):
            return text


async def check_users_which_should_be_notified(user_list):
    """проверяет юзеров, кто должен получить напоминание"""
    if datetime.now().strftime("%H:%M") == datetime.strptime("17:01", "%H:%M"):
        print('fuck yeah')
        for user in user_list:
            if send_reminder(user):
                await bot.send_message(chat_id=user, text=send_reminder(user))
