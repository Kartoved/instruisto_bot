from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Text
from keyboards.keyboards import *
from services.services import *


router = Router()


@router.callback_query(Text(text='get next word'))
async def add_word(callback: CallbackQuery):
    chat_id = callback.from_user.id
    await callback.answer()
    new_word = await get_unexplored_word(chat_id=chat_id)
    new_word = check_coefficient(new_word, new_word['коэффициент'])
    export_unexplored_words(chat_id)
    export_explored_words(chat_id, new_word)


@router.callback_query(Text(text='remember'))
async def remember_word(callback: CallbackQuery):
    chat_id = callback.from_user.id
    await callback.answer('bonege!')
    explored_words = import_explored_words(chat_id)
    word = get_explored_word(explored_words)
    explored_words.remove(word)
    word = check_and_change_coefficient(word, word['коэффициент'], True)
    export_explored_words(chat_id, word)
    await send_explored_word(chat_id, explored_words)


@router.callback_query(Text(text='forgot'))
async def forgot_word(callback: CallbackQuery):
    chat_id = callback.from_user.id
    await callback.answer()
    explored_words = import_explored_words(chat_id)
    word = get_explored_word(explored_words)
    explored_words.remove(word)
    word = check_and_change_coefficient(word, word['коэффициент'], False)
    export_explored_words(chat_id, word)
    await send_explored_word(chat_id, explored_words)


@router.callback_query(Text(text='stop'))
async def forgot_word(callback: CallbackQuery):
    chat_id = callback.from_user.id
    await callback.answer('trejnado ĉesis')
    await bot.send_message(text='Повторение слов остановлено', chat_id=chat_id)
