"""хендлеры"""
import json
from os import makedirs
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from lexicon.lexicon import HELP_COMMAND, get_profile_message, CONTACT, LINKS
from keyboards.keyboards import keybord_start, keyboard_profile, keyboard_cancel
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
    text: str = get_profile_message(message.from_user.username, explored_words, chat_id)
    await bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard_profile)


@router.message(Command(commands="learning"))
async def start_learning(message: Message):
    """начать учить неизученные слова"""
    chat_id: int = message.chat.id
    explored_words: list = s.import_words(chat_id, "explored_words")
    unexplored_words: list = s.import_words(chat_id, "unexplored_words")
    new_word: dict = await s.get_unexplored_word(chat_id, unexplored_words)
    if new_word:
        new_word = s.check_and_change_coefficient(new_word, new_word["интервал"])
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
    with open("reports/reports_statements.json", encoding="utf-8") as f:
        statements: dict = json.load(f)
    statements[chat_id] = True
    with open("reports/reports_statements.json", 'w', encoding="utf-8") as f:
        json.dump(statements, f)
    await bot.send_message(text=CONTACT,
                           chat_id=message.chat.id,
                           reply_markup=keyboard_cancel)


@router.message(Command(commands=["links"]))
async def send_useful_links(message: Message):
    """показать полезные ссылки"""
    await bot.send_message(text=LINKS,
                           chat_id=message.chat.id,
                           disable_web_page_preview=True)


@router.message()
async def send_report(message: Message):
    chat_id: int = message.chat.id
    mes: str = message.text
    with open("reports/reports_statements.json", encoding="utf-8") as file:
        statements: dict = json.load(file)
    try:
        if statements[str(chat_id)]:
            s.export_report(chat_id, mes, message.from_user.username)
            statements[f'{chat_id}'] = False
            with open("reports/reports_statements.json", 'w', encoding="utf-8") as file:
                json.dump(statements, file)
            await bot.send_message(chat_id=chat_id,
                                   text="😊 Спасибо! Твоё сообщение направлено моему разработчику")
    except KeyError:
        pass
