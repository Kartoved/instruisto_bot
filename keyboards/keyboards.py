'''клавиатуры для бота'''

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# кнопки
btn_accepting_reset = InlineKeyboardButton(
    text='✅ да, я уверен',
    callback_data='accepting reset'
)

btn_cancel = InlineKeyboardButton(
    text='⏹ отмена',
    callback_data='cancel'
)

btn_cancel_report = InlineKeyboardButton(
    text='⏹ отмена',
    callback_data='cancel report'
)

btn_delete_reminder = InlineKeyboardButton(
    text='❌  удалить напоминание',
    callback_data='delete reminder'
)

btn_stop = InlineKeyboardButton(
    text='⏹ стоп',
    callback_data='stop'
)

btn_add_word = InlineKeyboardButton(
    text='➡️ следующее слово',
    callback_data='get next unexplored word'
)

btn_forgot = InlineKeyboardButton(
    text='❌ не помню',
    callback_data='forgot'
)

btn_remember = InlineKeyboardButton(
    text='✅ помню',
    callback_data='remember'
)

btn_set_reminder = InlineKeyboardButton(
    text='⏰  напоминание',
    callback_data='set reminder'
)

btn_curve = InlineKeyboardButton(
    text='Кривая Эббингауза. Википедия',
    url='https://ru.wikipedia.org/wiki/Кривая_забывания'
)

btn_about_repeating = InlineKeyboardButton(
    text='Расскажи подробнее, как ты работаешь!',
    callback_data='about bot'
)

btn_open_profile = InlineKeyboardButton(
    text='👤 sinprezento',
    callback_data='stop'
)

keyboard_start = InlineKeyboardMarkup(
    inline_keyboard=[[btn_open_profile], [btn_curve], [btn_about_repeating]]
)

btn_mnemo = InlineKeyboardButton(
    text='Что ещё за мнемотехники такие?',
    callback_data='about mnemo'
)

keyboard_mnemo = InlineKeyboardMarkup(
    inline_keyboard=[[btn_open_profile], [btn_mnemo]]
)

# клавиатура профиля
btn_learning = InlineKeyboardButton(
    text='📖 учить новые слова', callback_data='start learning'
)

btn_repeating = InlineKeyboardButton(
    text='🔁 повторять слова', callback_data='start repeating'
)
btn_contact_with_dev = InlineKeyboardButton(
    text='📨 связь с разработчиком', callback_data='contact'
)
btn_reset_progress = InlineKeyboardButton(
    text='❌ сбросить прогресс', callback_data='reset progress'
)
btn_links = InlineKeyboardButton(
    text='🔗 полезные ссылки', callback_data='show_links'
)
btn_help = InlineKeyboardButton(
    text='❓ как это работает?', callback_data='help'
)
keyboard_profile = InlineKeyboardMarkup(
    inline_keyboard=[[btn_learning, btn_repeating],
                     [btn_reset_progress, btn_links],
                     [btn_help, btn_set_reminder],
                     [btn_contact_with_dev]],
)

# прочие клавиатуры
keyboard_reset = InlineKeyboardMarkup(
    inline_keyboard=[[btn_cancel, btn_accepting_reset]]
)

keyboard_cancel_report = InlineKeyboardMarkup(
    inline_keyboard=[[btn_cancel_report]]
)

keyboard_cancel = InlineKeyboardMarkup(
    inline_keyboard=[[btn_cancel]]
)

keyboard_open_profile = InlineKeyboardMarkup(
    inline_keyboard=[[btn_open_profile]]
)


keyboard_repeating = InlineKeyboardMarkup(
    inline_keyboard=[[btn_repeating]]
)


keyboard_set_reminder = InlineKeyboardMarkup(
    inline_keyboard=[[btn_delete_reminder], [btn_cancel_report]]
)

keyboard_check_word = InlineKeyboardMarkup(
    inline_keyboard=[[btn_forgot, btn_stop, btn_remember]]
)

keyboard_add_word = InlineKeyboardMarkup(
    inline_keyboard=[[btn_stop, btn_add_word]]
)
