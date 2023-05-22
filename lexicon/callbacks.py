from shutil import rmtree
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Text
from keyboards.keyboards import *
from services.services import *
from lexicon.lexicon import ABOUT_REPEATING, ABOUT_MNEMO, get_profile_message, RESET_MESSAGE


router = Router()


@router.callback_query(Text(text='get next unexplored word'))
async def get_next_unexplored_word(callback: CallbackQuery):
    chat_id = callback.from_user.id
    await callback.answer()
    unexplored_words = import_words(chat_id, 'unexplored_words')
    explored_words = import_words(chat_id, 'explored_words')
    new_word = await get_unexplored_word(chat_id, unexplored_words)
    if new_word:
        new_word = check_and_change_coefficient(
            new_word, new_word['коэффициент'])
        export_words(chat_id, unexplored_words, 'unexplored_words')
        if new_word not in explored_words:
            explored_words.append(new_word)
            export_words(chat_id, explored_words, 'explored_words')


@router.callback_query(Text(text='remember'))
async def remember(callback: CallbackQuery):
    chat_id = callback.from_user.id
    await callback.answer('bonege!')
    explored_words = import_words(chat_id, 'explored_words')
    word = get_explored_word(explored_words)
    explored_words.remove(word)
    word = check_and_change_coefficient(word, word['коэффициент'], True)
    if word not in explored_words:
        explored_words.append(word)
        export_words(chat_id, explored_words, 'explored_words')
    await send_explored_word(chat_id, explored_words)


@router.callback_query(Text(text='forgot'))
async def forgot(callback: CallbackQuery):
    chat_id = callback.from_user.id
    await callback.answer('Vi sukcesos!')
    explored_words = import_words(chat_id, 'explored_words')
    word = get_explored_word(explored_words)
    explored_words.remove(word)
    word = check_and_change_coefficient(word, word['коэффициент'], False)
    if word not in explored_words:
        explored_words.append(word)
        export_words(chat_id, explored_words, 'explored_words')
    await send_explored_word(chat_id, explored_words)


@router.callback_query(Text(text='about bot'))
async def tell_about_repeating(callback: CallbackQuery):
    await callback.answer('')
    await bot.send_message(text=ABOUT_REPEATING,
                           chat_id=callback.from_user.id,
                           reply_markup=keyboard_mnemo,
                           disable_web_page_preview=True)


@router.callback_query(Text(text='about mnemo'))
async def tell_about_repeating(callback: CallbackQuery):
    await callback.answer('')
    await bot.send_message(text=ABOUT_MNEMO,
                           chat_id=callback.from_user.id,
                           disable_web_page_preview=True)


@router.callback_query(Text(text='start repeating'))
async def start_repeating(callback: CallbackQuery):
    chat_id = callback.from_user.id
    await callback.answer('')
    explored_words = import_words(chat_id, 'explored_words')
    await send_explored_word(chat_id, explored_words)


@router.callback_query(Text(text='start learning'))
async def start_repeating(callback: CallbackQuery):
    chat_id = callback.from_user.id
    await callback.answer('')
    explored_words = import_words(chat_id, 'explored_words')
    unexplored_words = import_words(chat_id, 'unexplored_words')
    new_word = await get_unexplored_word(chat_id, unexplored_words)
    if new_word:
        new_word = check_and_change_coefficient(
            new_word, new_word['коэффициент'])
        export_words(chat_id, unexplored_words, 'unexplored_words')
        if new_word not in explored_words:
            explored_words.append(new_word)
            export_words(chat_id, explored_words, 'explored_words')


@router.callback_query(Text(text='stop'))
async def start_repeating(callback: CallbackQuery):
    chat_id = callback.from_user.id
    await callback.answer('')
    explored_words = import_words(chat_id, 'explored_words')
    text = get_profile_message(callback.from_user.username, explored_words)
    await bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard_profile)


@router.callback_query(Text(text='reset progress'))
async def process_reset_progress(callback: CallbackQuery):
    chat_id = callback.from_user.id
    await callback.answer('')
    await bot.send_message(chat_id=chat_id, text=RESET_MESSAGE, reply_markup=keyboard_reset)


@router.callback_query(Text(text='accepting reset'))
async def process_reset_progress(callback: CallbackQuery):
    chat_id = callback.from_user.id
    await callback.answer('')
    rmtree(f'users_data/{chat_id}')
    await bot.send_message(chat_id=chat_id, text=f'Ваш прогресс сброшен!')
