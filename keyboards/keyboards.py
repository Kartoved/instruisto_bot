from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)


# инлайн-клавиатура для связи с разработчиком 
btn_contact = InlineKeyboardButton(
    text='связаться с разработчиком'.capitalize(),
    url='https://ru.wikipedia.org/wiki/Эсперанто')

keyboard_contact = InlineKeyboardMarkup(
    inline_keyboard=[[btn_contact]])


# инлайн-клавиатура добавить слово в список знакомых слов
btn_add_word = InlineKeyboardButton(
    text='следующее слово',
    callback_data='get next word')

keyboard_add_word = InlineKeyboardMarkup(inline_keyboard=[[btn_add_word]])

# инлайн-клавиатура для помню/не помню
btn_forgot = InlineKeyboardButton(
    text='не помню',
    url='https://ru.wikipedia.org/wiki/Эсперанто')
btn_remember = InlineKeyboardButton(
    text='помню',
    callback_data='помню')

keyboard_check_word = InlineKeyboardMarkup(
    inline_keyboard=[[btn_forgot, btn_remember]])