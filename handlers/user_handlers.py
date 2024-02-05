"""хендлеры"""
import json
import asyncio
import aioschedule
from os import makedirs
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from lexicon.lexicon import HELP_COMMAND, get_profile_message, CONTACT, LINKS
from keyboards.keyboards import keybord_start, keyboard_profile, keyboard_cancel, keyboard_open_profile, keyboard_cancel_report
from config_data.config import bot
import services.services as s

router: Router = Router()
statements = {}


@router.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    """запуск бота, создание необходимых файлов"""
    chat_id: int = message.chat.id
    s.create_user_folders(chat_id)
    s.add_user_to_list(chat_id)
    await message.answer(text=HELP_COMMAND, reply_markup=keybord_start)


@router.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    """вывод приветствия и справки"""
    await message.answer(text=HELP_COMMAND, reply_markup=keybord_start)


@router.message(Command(commands=["stop", "profile"]))
async def show_profile(message: Message):
    """выводит профиль юзера"""
    chat_id: int = message.chat.id
    explored_words: list = s.import_words(chat_id, "explored_words")
    text: str = get_profile_message(
        message.from_user.username, explored_words, chat_id)
    await bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard_profile)


@router.message(Command(commands="learning"))
async def start_learning(message: Message):
    """начать учить неизученные слова"""
    chat_id: int = message.chat.id
    explored_words: list = s.import_words(chat_id, "explored_words")
    unexplored_words: list = s.import_words(chat_id, "unexplored_words")
    new_word: dict = await s.get_unexplored_word(chat_id, unexplored_words)
    if new_word:
        new_word = s.check_and_change_coefficient(
            new_word, new_word["интервал"])
        s.export_words(chat_id, unexplored_words, "unexplored_words")
        if new_word not in explored_words:
            explored_words.append(new_word)
            s.export_words(chat_id, explored_words, "explored_words")


@router.message(Command(commands="repeating"))
async def start_repeating(message: Message):
    """повторение изученных слов"""
    chat_id: int = message.chat.id
    explored_words: list = s.import_words(chat_id, "explored_words")
    await s.send_explored_word(chat_id, explored_words)


@router.message(Command(commands=["contact"]))
async def write_message_to_dev(message: Message):
    """написать сообщение разработчику"""
    chat_id: int = message.chat.id
    with open("users_data/statements.json", encoding="utf-8") as f:
        statements: dict = json.load(f)
    statements[chat_id] = 1
    with open("users_data/statements.json", 'w', encoding="utf-8") as f:
        json.dump(statements, f)
    await bot.send_message(text=CONTACT,
                           chat_id=chat_id,
                           reply_markup=keyboard_cancel_report)


@router.message(Command(commands=["links"]))
async def send_useful_links(message: Message):
    """показать полезные ссылки"""
    await bot.send_message(text=LINKS,
                           chat_id=message.chat.id,
                           disable_web_page_preview=True,
                           reply_markup=keyboard_open_profile)


@router.message()
async def send_report(message: Message):
    chat_id: int = message.chat.id
    mes: str = message.text
    with open("users_data/statements.json", encoding="utf-8") as f:
        statements: dict = json.load(f)
    with open("users_data/reminders.json", encoding="utf-8") as f:
        reminders = json.load(f)
    try:
        if statements[str(chat_id)] == 1:
            s.export_report(chat_id, mes, message.from_user.username)
            statements[f'{chat_id}'] = 0
            with open("users_data/statements.json", 'w', encoding="utf-8") as f:
                json.dump(statements, f)
            await bot.send_message(chat_id=chat_id,
                                   text="😊 Спасибо! Твоё сообщение направлено моему разработчику.")
        elif statements[str(chat_id)] == 2:
            if s.check_input_time(mes):
                reminders[f'{chat_id}'] = mes
                statements[f'{chat_id}'] = 0
                with open("users_data/reminders.json", 'w', encoding="utf-8") as f:
                    json.dump(reminders, f)
                with open("users_data/statements.json", 'w', encoding="utf-8") as f:
                    json.dump(statements, f)
                s.run_scheduler()
                await bot.send_message(chat_id=chat_id, text="✅ Напоминание установлено. Ты можешь всегда изменить или удалить его.")
            else:
                await bot.send_message(chat_id=chat_id, text="❌ Время введено некорректно! Введите время в формате <strong>чч:мм</strong>!")
    except KeyError:
        pass




