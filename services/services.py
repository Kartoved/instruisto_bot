"""необходимые функции"""

import json
from shutil import copy, make_archive
from aiogram.types import FSInputFile
from os import makedirs, rename, path
from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config_data.config import bot
import keyboards.keyboards as k

scheduler = AsyncIOScheduler()
with open("users_data/admin_list.json", encoding="utf-8") as f:
    admin_list = json.load(f)

# backup = make_archive(
#         base_name="backup", format="zip", root_dir="users_data", base_dir="."
#     )


# async def send_archive_to_dev(bot: bot, admins_ids):
#     """отправить архив"""
#     backup = make_archive(
#         base_name="backup", format="zip", root_dir="users_data", base_dir="."
#     )
#     for admin in admins_ids:
#         await bot.send_document(
#             chat_id=admin, document=FSInputFile(backup), caption="#бэкап данных юзеров"
#         )


# for admin in admin_list:
#     scheduler.add_job(
#         send_archive_to_dev,
#         trigger="cron",
#         hour=00,
#         minute=00,
#         replace_existing=True,
#         kwargs={"bot": bot, "chat_id": admin},
#     )


async def send_archive(admins_ids):
    """отправить архив"""
    backup = make_archive(
        base_name="backup", format="zip", root_dir="users_data", base_dir="."
    )
    for admin in admins_ids:
        await bot.send_document(
            chat_id=admin, document=FSInputFile(backup), caption="#бэкап данных юзеров"
        )


scheduler = AsyncIOScheduler()
with open("users_data/admin_list.json", encoding="utf-8") as f:
    admin_list = json.load(f)


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
    if not path.exists("users_data/admin_list.json"):
        with open("users_data/admin_list.json", "w", encoding="utf-8") as f:
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


def run_scheduler(scheduler):
    """запускает планировщик"""
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
        if man in who_needs_reminder:
            scheduler.add_job(
                send_message_cron,
                trigger="cron",
                hour=value[0:2],
                minute=value[3:5],
                id=man,
                kwargs={"bot": bot, "chat_id": man},
            )
    scheduler.start()


def add_job_to_scheduler(scheduler, mes, chat_id):
    """добавляет задание в планировщик"""
    scheduler.add_job(
        send_message_cron,
        trigger="cron",
        hour=mes[0:2],
        minute=mes[3:5],
        id=str(chat_id),
        replace_existing=True,
        kwargs={"bot": bot, "chat_id": chat_id},
    )


async def send_message_to_all_users(mes):
    with open("users_data/user_list.json", encoding="utf-8") as f:
        user_list = json.load(f)
    for user in user_list:
        await bot.send_message(chat_id=user, text=mes[4:])


async def send_message_to_dev(mes, chat_id, statements, admin_list):
    statements[f"{chat_id}"] = 0
    with open("users_data/statements.json", "w", encoding="utf-8") as f:
        json.dump(statements, f)
    await bot.send_message(
        chat_id=chat_id,
        text="😊 Спасибо! Твоё сообщение направлено моему разработчику.",
    )
    for admin in admin_list:
        await bot.send_message(
            chat_id=admin,
            text=f"#Фидбек от https://t.me/{mes.from_user.username}: \n\n{mes.html_text}",
        )
