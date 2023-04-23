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
