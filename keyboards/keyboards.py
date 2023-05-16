from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# инлайн-клавиатура добавить слово в список знакомых слов
btn_add_word = InlineKeyboardButton(
    text='➡️ следующее слово',
    callback_data='get next unexplored word')

keyboard_add_word = InlineKeyboardMarkup(
    inline_keyboard=[[btn_add_word]])

# инлайн-клавиатура для помню/не помню
btn_forgot = InlineKeyboardButton(
    text='❌ не помню',
    callback_data='forgot')
btn_remember = InlineKeyboardButton(
    text='✅ помню',
    callback_data='remember')
keyboard_check_word = InlineKeyboardMarkup(
    inline_keyboard=[[btn_forgot, btn_remember]])


# инлайн-клавиатура для старта
btn_curve = InlineKeyboardButton(
    text='Кривая Эббингауза. Википедия',
    url='https://ru.wikipedia.org/wiki/Кривая_забывания')
btn_about_repeating = InlineKeyboardButton(text='Расскажи подробнее, как ты работаешь!',
                                           callback_data='tell me')

keybord_start = InlineKeyboardMarkup(
    inline_keyboard=[[btn_curve], [btn_about_repeating]])
