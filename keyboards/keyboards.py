from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)


# инлайн-клавиатура добавить слово в список знакомых слов
btn_stop_learning = InlineKeyboardButton(
    text='⏹ стоп',
    callback_data='stop learning')
btn_add_word = InlineKeyboardButton(
    text='➡️ следующее слово',
    callback_data='get next unexplored word')

keyboard_add_word = InlineKeyboardMarkup(
    inline_keyboard=[[btn_stop_learning, btn_add_word]])

# инлайн-клавиатура для помню/не помню
btn_forgot = InlineKeyboardButton(
    text='❌ не помню',
    callback_data='forgot')
btn_remember = InlineKeyboardButton(
    text='✅ помню',
    callback_data='remember')
btn_stop_repeating = InlineKeyboardButton(
    text='⏹ стоп',
    callback_data='stop repeating')
keyboard_check_word = InlineKeyboardMarkup(
    inline_keyboard=[[btn_forgot, btn_stop_repeating, btn_remember]])


# инлайн-клавиатура для старта
btn_curve = InlineKeyboardButton(
    text='Кривая Эббингауза. Википедии',
    url='https://ru.wikipedia.org/wiki/Кривая_забывания')

keybord_start = InlineKeyboardMarkup(
    inline_keyboard=[[btn_curve]])
