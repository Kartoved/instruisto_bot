"""необходимые функции"""

import json
from shutil import copy
from os import makedirs, rename, path
from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config_data.config import bot
import keyboards.keyboards as k
import lexicon.lexicon as L


# функции для хендлеров и коллбэков


# асинхронные функции
async def get_unexplored_word(chat_id: int, unexplored_words: list) -> dict:
    """выдаёт одно слово из списка неизученных"""
    if unexplored_words:
        new_word: dict = unexplored_words.pop(0)
        await bot.send_message(
            text=L.format_learning_message(new_word),
            chat_id=chat_id,
            reply_markup=k.keyboard_add_word,
        )
    else:
        new_word: dict = {}
        await bot.send_message(
            text="Все слова изучены. Новых слов нет.", chat_id=chat_id
        )
    return new_word


async def send_explored_word(chat_id: int, explored_words: list) -> dict:
    """отправить пользователю изученное слово"""
    for word in explored_words:
        if datetime.strptime(word["дата повторения"], "%d-%m-%Y") <= datetime.now():
            return await bot.send_message(
                text=L.format_repeating_message(word),
                chat_id=chat_id,
                reply_markup=k.keyboard_check_word,
            )
    date_of_closest_repetition = L.get_date_of_closest_repetition(explored_words)
    return await bot.send_message(
        text=date_of_closest_repetition,
        chat_id=chat_id,
        reply_markup=k.keyboard_open_profile,
    )


async def send_message_cron(bot: bot, chat_id: int):
    """присылает напоминание в указанное время"""
    await bot.send_message(
        chat_id, text="Пора повторять слова!", reply_markup=k.keyboard_repeating
    )


# обычные функции
def change_date(value: int) -> str:
    """меняет дату повторения слова"""
    date: datetime = datetime.now()
    date = date + timedelta(days=value)
    return date.strftime("%d-%m-%Y")


def check_and_change_coefficient(
    word: dict, interval: int, remember: bool = False
) -> dict:
    """проверяет текущий интервал и изменяет его"""
    if remember and interval < 6:
        interval += 1
    elif not remember and interval > 0:
        interval -= 1
    word["интервал"]: int = interval
    interval_to_days = [1, 2, 7, 14, 28, 84, 168]
    word["дата повторения"] = str(change_date(interval_to_days[interval]))
    return word


def get_explored_word(explored_words: list) -> dict:
    """выдаёт слово из списка изученных"""
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
    if not path.exists("users_data/statements.json"):
        with open("users_data/statements.json", "w", encoding="utf-8") as f:
            json.dump({}, f)
    if not path.exists("users_data/reminders.json"):
        with open("users_data/reminders.json", "w", encoding="utf-8") as f:
            json.dump({}, f)
    if not path.exists("users_data/user_list.json"):
        with open("users_data/user_list.json", "w", encoding="utf-8") as f:
            json.dump([], f)


def create_user_folders(chat_id: int):
    """создаёт папку пользователя"""
    if not path.exists(f"users_data/{chat_id}"):
        makedirs(f"users_data/{chat_id}", exist_ok=True)
        copy("services/dictionary.json", f"users_data/{chat_id}")
        rename(
            f"users_data/{chat_id}/dictionary.json",
            f"users_data/{chat_id}/unexplored_words.json",
        )
        with open(
            f"users_data/{chat_id}/explored_words.json", mode="w", encoding="utf-8"
        ) as f:
            json.dump([], f)


def add_user_to_list(chat_id):
    """добавляет юзера в список юзеров"""
    try:
        with open("users_data/user_list.json", encoding="utf-8") as f:
            user_list: list = json.load(f)
            if chat_id not in user_list:
                user_list.append(chat_id)
                with open("users_data/user_list.json", "w", encoding="utf-8") as f:
                    json.dump(user_list, f)
    except FileNotFoundError:
        with open("users_data/user_list.json", "w", encoding="utf-8") as f:
            user_list: list = [chat_id]
            json.dump(user_list, f)


def export_report(chat_id: int, report: str, username: str):
    """экспортирует багрепорт в файл"""
    date = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    with open(f"reports/{date}.txt", "w", encoding="utf-8") as f:
        f.write(f'from user: {username}\n\n"{report}"')


def check_input_time(text: str) -> bool:
    """проверяет введённое время"""
    try:
        datetime.strptime(text, "%H:%M")
        return True
    except ValueError:
        return False


def run_scheduler():
    """запускает планировщик"""
    scheduler = AsyncIOScheduler()
    with open("users_data/reminders.json", "r", encoding="utf-8") as f:
        reminders = json.load(f)
    who_needs_reminder: list = []
    for key in reminders.keys():
        with open(f"users_data/{key}/explored_words.json", encoding="utf-8") as f:
            explored_words = json.load(f)
        for word in explored_words:
            if datetime.strptime(word["дата повторения"], "%d-%m-%Y").strftime(
                "%d-%m-%Y"
            ) <= datetime.now().strftime("%d-%m-%Y"):
                who_needs_reminder.append(key)
    for man, value in reminders.items():
        scheduler.remove_all_jobs()
        if man in who_needs_reminder:
            # scheduler.remove_all_jobs()
            scheduler.add_job(
                send_message_cron,
                trigger="cron",
                hour=value[0:2],
                minute=value[3:5],
                kwargs={"bot": bot, "chat_id": man},
            )
    scheduler.start()
