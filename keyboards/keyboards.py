from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# инлайн-клавиатура добавить слово в список знакомых слов
btn_stop = InlineKeyboardButton(
    text='⏹ стоп',
    callback_data='stop')
btn_add_word = InlineKeyboardButton(
    text='➡️ следующее слово',
    callback_data='get next unexplored word')

keyboard_add_word = InlineKeyboardMarkup(
    inline_keyboard=[[btn_stop, btn_add_word]])

# инлайн-клавиатура для помню/не помню
btn_forgot = InlineKeyboardButton(
    text='❌ не помню',
    callback_data='forgot')
btn_remember = InlineKeyboardButton(
    text='✅ помню',
    callback_data='remember')
keyboard_check_word = InlineKeyboardMarkup(
    inline_keyboard=[[btn_forgot, btn_stop, btn_remember]])


# инлайн-клавиатура для старта
btn_curve = InlineKeyboardButton(
    text='Кривая Эббингауза. Википедия',
    url='https://ru.wikipedia.org/wiki/Кривая_забывания')
btn_about_repeating = InlineKeyboardButton(text='Расскажи подробнее, как ты работаешь!',
                                           callback_data='about bot')

keybord_start = InlineKeyboardMarkup(
    inline_keyboard=[[btn_curve], [btn_about_repeating]])

btn_mnemo = InlineKeyboardButton(text='Что ещё за мнемотехники такие?',
                                 callback_data='about mnemo')
keyboard_mnemo = InlineKeyboardMarkup(inline_keyboard=[[btn_mnemo]])

# клавиатура профиля
btn_learning = InlineKeyboardButton(
    text='📖 учить новые слова', callback_data='start learning')
btn_repeating = InlineKeyboardButton(
    text='🔁 повторять слова', callback_data='start repeating')
btn_contact_with_dev = InlineKeyboardButton(
    text='📨 связь с разработчиком', callback_data='contact')
btn_reset_progress = InlineKeyboardButton(
    text='❌ сбросить прогресс', callback_data='reset progress')
btn_help = InlineKeyboardButton(
    text='❓ как это работает?', callback_data='help')
keyboard_profile = InlineKeyboardMarkup(
    inline_keyboard=[[btn_learning, btn_repeating],
                     [btn_reset_progress, btn_contact_with_dev],
                     [btn_help]])

# клавиатура для удаления прогресса профиля
btn_accepting_reset = InlineKeyboardButton(
    text='✅ Да, я уверен. Удали весь мой прогресс',
    callback_data='accepting reset'
)

btn_cancel = InlineKeyboardButton(
    text='⏹ отмена',
    callback_data='cancel'
)

keyboard_reset = InlineKeyboardMarkup(
    inline_keyboard=[[btn_cancel, btn_accepting_reset]]
)
