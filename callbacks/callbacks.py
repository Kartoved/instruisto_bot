'''коллбэки'''

import json
from shutil import rmtree
from aiogram import Router, F
from aiogram.types import CallbackQuery
from config_data.config import bot
import keyboards.keyboards as k
import services.services as s
import lexicon.lexicon as L


router = Router()
statements = {}


@router.callback_query(F.data == 'get next unexplored word')
async def get_next_unexplored_word(callback: CallbackQuery):
    '''выдаёт следующее неизученное слово'''
    chat_id: int = callback.from_user.id
    await callback.answer()
    unexplored_words: list = s.import_words(chat_id, 'unexplored_words')
    explored_words: list = s.import_words(chat_id, 'explored_words')
    new_word: dict = await s.get_unexplored_word(chat_id, unexplored_words)
    if new_word:
        new_word = s.check_and_change_coefficient(
            new_word, new_word['интервал'])
        s.export_words(chat_id, unexplored_words, 'unexplored_words')
        if new_word not in explored_words:
            explored_words.append(new_word)
            s.export_words(chat_id, explored_words, 'explored_words')


@router.callback_query(F.data == 'remember')
async def remember(callback: CallbackQuery):
    '''срабатывает, если юзер помнит слово'''
    chat_id: int = callback.from_user.id
    await callback.answer('bonege!')
    explored_words: list = s.import_words(chat_id, 'explored_words')
    word: dict = s.get_explored_word(explored_words)
    explored_words.remove(word)
    word: dict = s.check_and_change_coefficient(
        word, word['интервал'], True)
    if word not in explored_words:
        explored_words.append(word)
        s.export_words(chat_id, explored_words, 'explored_words')
    await s.send_explored_word(chat_id, explored_words)


@router.callback_query(F.data == 'forgot')
async def forgot(callback: CallbackQuery):
    '''срабатывает, если юзер не помнит слова'''
    chat_id: int = callback.from_user.id
    await callback.answer('Vi sukcesos!')
    explored_words: list = s.import_words(chat_id, 'explored_words')
    word: dict = s.get_explored_word(explored_words)
    explored_words.remove(word)
    word: dict = s.check_and_change_coefficient(
        word, word['интервал'], False)
    if word not in explored_words:
        explored_words.append(word)
        s.export_words(chat_id, explored_words, 'explored_words')
    await s.send_explored_word(chat_id, explored_words)


@router.callback_query(F.data == 'about bot')
async def tell_about_bot(callback: CallbackQuery):
    '''рассказывает о принципе работы бота'''
    await callback.answer('')
    await bot.send_message(text=L.ABOUT_REPEATING,
                           chat_id=callback.from_user.id,
                           reply_markup=k.keyboard_mnemo,
                           disable_web_page_preview=True)


@router.callback_query(F.data == 'about mnemo')
async def tell_about_mnemo(callback: CallbackQuery):
    '''рассказывает про мнемотехники'''
    await callback.answer('')
    await bot.send_message(text=L.ABOUT_MNEMO,
                           chat_id=callback.from_user.id,
                           disable_web_page_preview=True,
                           reply_markup=k.keyboard_open_profile)


@router.callback_query(F.data == 'help')
async def process_help_command(callback: CallbackQuery):
    '''справка со всеми командами'''
    await callback.answer('')
    await bot.send_message(text=L.HELP_COMMAND,
                           chat_id=callback.from_user.id,
                           reply_markup=k.keyboard_start)


@router.callback_query(F.data == 'start repeating')
async def start_repeating(callback: CallbackQuery):
    '''инициирует процесс повторения изученных слов'''
    chat_id: int = callback.from_user.id
    await callback.answer('')
    explored_words: list = s.import_words(chat_id, 'explored_words')
    await s.send_explored_word(chat_id, explored_words)


@router.callback_query(F.data == 'start learning')
async def start_learning(callback: CallbackQuery):
    '''инициирует процесс изучения новых слов'''
    chat_id: int = callback.from_user.id
    await callback.answer('')
    explored_words: list = s.import_words(chat_id, 'explored_words')
    unexplored_words: list = s.import_words(chat_id, 'unexplored_words')
    new_word: dict = await s.get_unexplored_word(chat_id, unexplored_words)
    if new_word:
        new_word = s.check_and_change_coefficient(
            new_word, new_word['интервал'])
        s.export_words(chat_id, unexplored_words, 'unexplored_words')
        if new_word not in explored_words:
            explored_words.append(new_word)
            s.export_words(chat_id, explored_words, 'explored_words')


@router.callback_query(F.data == 'stop')
async def stop_repeating(callback: CallbackQuery):
    '''останавливает тренировку'''
    chat_id: int = callback.from_user.id
    await callback.answer('')
    explored_words: list = s.import_words(chat_id, 'explored_words')
    text: str = L.get_profile_message(
        callback.from_user.username, explored_words, chat_id)
    await bot.send_message(chat_id=chat_id,
                           text=text,
                           reply_markup=k.keyboard_profile)


@router.callback_query(F.data == 'cancel')
async def cancel_reset(callback: CallbackQuery):
    '''отменяет процесс сброса прогресса'''
    chat_id: int = callback.from_user.id
    await callback.answer('отмена')
    explored_words: list = s.import_words(chat_id, 'explored_words')
    text: str = L.get_profile_message(callback.from_user.username,
                                      explored_words,
                                      chat_id)
    await callback.message.edit_text(text=text, reply_markup=k.keyboard_profile)


@router.callback_query(F.data == 'cancel report')
async def cancel_report(callback: CallbackQuery):
    chat_id: int = callback.from_user.id
    with open("users_data/statements.json", encoding="utf-8") as f:
        statements = json.load(f)
        statements[str(chat_id)] = 0
    with open("users_data/statements.json", 'w', encoding="utf-8") as f:
        json.dump(statements, f)
    await callback.answer('')
    await callback.message.delete()


@router.callback_query(F.data == 'reset progress')
async def process_reset_progress(callback: CallbackQuery):
    '''запрашивает подтверждение сброса прогресса'''
    await callback.answer('')
    await callback.message.edit_text(text=L.RESET_MESSAGE,
                                     reply_markup=k.keyboard_reset)


@router.callback_query(F.data == 'accepting reset')
async def accept_reset(callback: CallbackQuery):
    '''подтверждаем процесс сброса прогресса'''
    chat_id: int = callback.from_user.id
    explored_words: list = s.import_words(callback.from_user.id,
                                          'explored_words')
    await callback.answer('Принято')
    rmtree(f'users_data/{chat_id}')
    s.create_user_folders(chat_id)
    await callback.message.edit_text(text=f'{callback.from_user.username}, твой прогресс сброшен!',
                                     reply_markup=k.keyboard_open_profile)


@router.callback_query(F.data == 'contact')
async def write_message_to_dev(callback: CallbackQuery):
    '''написать сообщение разработчику'''
    chat_id: int = callback.from_user.id
    with open("users_data/statements.json", encoding="utf-8") as f:
        statements = json.load(f)
        statements[str(chat_id)] = 1
    with open("users_data/statements.json", 'w', encoding="utf-8") as f:
        json.dump(statements, f)
    await callback.answer('')
    await bot.send_message(text=L.CONTACT,
                           chat_id=chat_id,
                           reply_markup=k.keyboard_cancel_report)


@router.callback_query(F.data == 'show_links')
async def send_useful_links(callback: CallbackQuery):
    '''показать полезные ссылки'''
    explored_words: list = s.import_words(callback.from_user.id,
                                          'explored_words')
    await callback.answer('')
    await bot.send_message(text=L.LINKS,
                           chat_id=callback.from_user.id,
                           disable_web_page_preview=True,
                           reply_markup=k.keyboard_open_profile)


@router.callback_query(F.data == 'set reminder')
async def set_reminder(callback: CallbackQuery):
    '''установить напоминание'''
    chat_id: int = callback.from_user.id
    with open("users_data/statements.json", encoding="utf-8") as f:
        statements = json.load(f)
        statements[str(chat_id)] = 2
    with open("users_data/statements.json", 'w', encoding="utf-8") as f:
        json.dump(statements, f)
    exists_reminder = L.get_time_of_reminder(chat_id)
    await callback.answer('')
    await bot.send_message(text=f'{exists_reminder}\n\nНапиши время, в которое должно приходить напоминание, в формате <strong>чч:мм</strong>.\nЛибо удали напоминание',
                           chat_id=chat_id,
                           reply_markup=k.keyboard_set_reminder)


@router.callback_query(F.data == 'delete reminder')
async def delete_reminder(callback: CallbackQuery):
    '''удалить напоминание'''
    chat_id: int = callback.from_user.id
    await callback.answer('')
    with open("users_data/reminders.json", encoding="utf-8") as f:
        reminders = json.load(f)
        try:
            del reminders[str(chat_id)]
            with open("users_data/reminders.json", 'w', encoding="utf-8") as f:
                json.dump(reminders, f)
            s.scheduler.remove_job(str(chat_id))
            print(s.scheduler.get_jobs())
            await callback.message.edit_text(text='✅ Напоминание удалено',
                                             reply_markup=k.keyboard_open_profile)
        except KeyError:
            await callback.message.edit_text(text='У тебя и не было напоминаний',
                                             reply_markup=k.keyboard_open_profile)
