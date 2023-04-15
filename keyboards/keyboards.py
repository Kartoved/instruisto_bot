from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)

btn_contact: InlineKeyboardButton = InlineKeyboardButton(
    text='связаться с разработчиком'.capitalize(),
    url='https://ru.wikipedia.org/wiki/Эсперанто')

keyboard_contact: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[btn_contact]])
