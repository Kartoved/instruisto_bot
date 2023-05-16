from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Text
from keyboards.keyboards import *
from services.services import *
from lexicon.lexicon import ABOUT_REPEATING


router = Router()


@router.callback_query(Text(text='get next unexplored word'))
async def get_next_unexplored_word(callback: CallbackQuery):
    chat_id = callback.from_user.id
    hashed_id = get_hashed_id(chat_id)
    await callback.answer()
    unexplored_words = import_words(hashed_id, 'unexplored_words')
    explored_words = import_words(hashed_id, 'explored_words')
    new_word = await get_unexplored_word(chat_id, unexplored_words)
    if new_word:
        new_word = check_and_change_coefficient(
            new_word, new_word['коэффициент'])
        export_words(hashed_id, unexplored_words, 'unexplored_words')
        if new_word not in explored_words:
            explored_words.append(new_word)
            export_words(hashed_id, explored_words, 'explored_words')


@router.callback_query(Text(text='remember'))
async def remember(callback: CallbackQuery):
    chat_id = callback.from_user.id
    hashed_id = get_hashed_id(chat_id)
    await callback.answer('bonege!')
    explored_words = import_words(hashed_id, 'explored_words')
    word = get_explored_word(explored_words)
    explored_words.remove(word)
    word = check_and_change_coefficient(word, word['коэффициент'], True)
    if word not in explored_words:
        explored_words.append(word)
        export_words(hashed_id, explored_words, 'explored_words')
    await send_explored_word(chat_id, explored_words)


@router.callback_query(Text(text='forgot'))
async def forgot(callback: CallbackQuery):
    chat_id = callback.from_user.id
    hashed_id = get_hashed_id(chat_id)
    await callback.answer()
    explored_words = import_words(hashed_id, 'explored_words')
    word = get_explored_word(explored_words)
    explored_words.remove(word)
    word = check_and_change_coefficient(word, word['коэффициент'], False)
    if word not in explored_words:
        explored_words.append(word)
        export_words(hashed_id, explored_words, 'explored_words')
    await send_explored_word(chat_id, explored_words)


@router.callback_query(Text(text='tell me'))
async def tell_about_repeating(callback: CallbackQuery):
    await callback.answer('')
    await bot.send_message(text=ABOUT_REPEATING,
                           chat_id=callback.from_user.id)
