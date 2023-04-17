from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Text
from keyboards.keyboards import *
# from services.services import add_word_to_expored_words


router = Router()

@router.callback_query(Text(text='add'))
async def add_word(callback: CallbackQuery):
    chat_id = callback.from_user.id
    await callback.answer(text='работает, епта!')
    # await add_word_to_expored_words(chat_id=chat_id)
