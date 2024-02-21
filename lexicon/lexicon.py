'''различный текст для бота'''

from datetime import datetime
import json


LINKS: str = '''🔗 Полезные ссылки:
• <a href="https://t.me/babilejo_eo_ru">Чат эсперантистов в телеграм</a> 
• <a href="https://vk.com/priesperanto">Паблик Эсперанто ВК</a> 
• <a href="https://vk.com/por_pigruloj">Паблик ВК "Эсперанто для лентяев"</a> 
• <a href="https://lernu.net/">Многоязычный сайт для изучения международного языка эсперанто</a> 
• <a href="https://kurso.com.br/index.php?ru">Курс обучения Эсперанто. Приложение для Android, Windows, Mac, Linux</a> 

Список будет пополняться. '''

HELP_COMMAND: str = '''👋 Привет, начинающий <em>эсперантист</em>!
Я бот-преподаватель языка <strong>Эсперанто</strong>.
Я помогу тебе выучить этот прекрасный язык!
Ознакомься с моими командами ниже (все команды кликабельны)👇:

<strong>/sinprezento</strong> — <em>👤 профиль</em>
<strong>/helpo</strong> — <em>🗒 список команд</em>
<strong>/memorigilo</strong> —  <em>⏰ установить напоминание</em>
<strong>/kontakti</strong> — <em>📨 связь с разработчиком</em>
<strong>/ligiloj</strong> — <em>🔗 полезные ссылки на материалы, где ты можешь изучать Эсперанто</em>

Следующие две команды помогут тебе выучить 1194 самых употребительных слова \
на <em>Эсперанто</em>. Для этого мы с тобой будем учить новые слова \
и повторять их через увеличивающиеся промежутки времени. \
За основу метода взята 📈 кривая Эббингауза, но немного модифицированная \
моим разработчиком. 
<strong>/vortstudi</strong> - <em>🧠 учить новые слова</em>
<strong>/parkerigi</strong> - <em>🔁 повторять изученные слова</em>

Также эти кнопки доступны в <em>меню бота</em> и в <em>профиле</em>.
'''

ABOUT_REPEATING: str = '☝️ Сначала ты учишь слова, используя команду \
<strong>/vortstudi</strong>. Не надо учить сразу все, начни с пяти слов, \
капля точит камень. Просто читаешь слово и стараешься его запомнить. \
Будет вдвойне полезно, если ты будешь использовать мнемотехники.\n\n\
Далее это слово попадает в список для повторения. Слова из этого списка \
доступны по команде <strong>/parkerigi</strong>. Слова там будут попадаться \
через разные промежутки времени: если ты нажимаешь на "✅ помню", \
то интервал будет увеличиваться. Если на "❌ не помню" — уменьшаться. \
Минимальный интервал — один день. Максимальный — 24 недели.\n\n\
🏋️ Старайся заниматься регулярно. Если каждый день учить по 5 слов,\
то через 239 дней будешь знать все 1194 слова из списка! \
Этого хватит для базового повседневного общения. 😊\n\n\
Разработчик: <a href="https://t.me/prepod_wood">Вуд Романов</a>\n\n\
🤗 Благодарности:\n• Список слов взят из подборки слов Владимира К. \
(ник incredibletroth) <a href="https://quizlet.com/incredibletroth/sets">на сайте Quizlet</a>.\n\
• Примеры предложений сконструированы ChatGPT.\n• Корректировщики-эсперантисты: <a href="https://vk.com/sskumkov">Сергей Кумков</a>,\
<a href="https://t.me/legado_eo_ru">Tatjana</a>, Aleksei Samsonov, <a href="https://t.me/eteveto">Va</a>.\n\
 • Аватарка бота сгенерирована Midjourney и изменена моим разработчиком\n • Спасибо всем, кто участвовал в тестировании!'

ABOUT_MNEMO: str = '☝️ Мнемотехника, или мнемоника, — это совокупность \
приёмов, увеличивающих объём памяти и облегчающих запоминание информации, \
основанная на создании образов и ассоциаций. Мнемотехники можно использовать \
для запоминания чего угодно.\n\n🔗 Ниже ссылки, как можно использовать их \
для запоминания иностранных слов:\n\n<a href="https://youtu.be/-uMqUe55v-M">\
• видео на ютубе</a>\n<a href="https://youtu.be/gh3NCuZHVrg">• ещё одно видео</a> \
\n<a href="https://habr.com/ru/articles/156599/">• статья на хабре</a>\n\n\
☝️ Кроме этих материалов есть и множество других. Изучи вопрос, \
это крутая тема, которая пригодится тебе во многих сферах жизни!'

CONTACT: str = '🪲 Нашёл баг или ошибку?\n💡 Есть идеи для улучшения?\n\
😊 Тебе всё нравится, просто хочешь сказать спасибо?\
\n🖌 Напиши об этом моему разработчику ответным сообщением в этом чате. Используй только текст, вложения пересылать я пока не умею.\
Если передумал, то нажми <em>"отмена"</em>'

LEXICON_COMMANDS_RU: dict[str, str] = {
    "/sinprezento": "👤 профиль",
    "/helpo": "❓ описание бота, список команд",
    "/vortstudi": "📖 учить новые слова",
    "/parkerigi": "🔁 повторять изученные слов",
    "/memorigilo": "⏰ установить напоминание",
    "/ligiloj": "🔗 полезные ссылки",
    "/kontakti": "📨 связь с разработчиком",    
}

ABOUT_UPDATE: str = f""


RESET_MESSAGE: str = "‼️‼️‼️ Вы уверены, что хотите сбросить прогресс? ‼️‼️‼️\
\n\nЭто действие НЕОБРАТИМО! Сбросится статистика, удалятся все изученные\
 слова и придётся учить их заново!"


def get_date_of_closest_repetition(explored_words: list) -> str:
    '''получить дату ближайшего повторения'''
    try:
        date_of_closest_repetition = datetime.strptime(
            explored_words[0]["дата повторения"], "%d-%m-%Y")
        for word in explored_words:
            if datetime.strptime(word["дата повторения"], "%d-%m-%Y") < date_of_closest_repetition:
                date_of_closest_repetition = datetime.strptime(
                    word["дата повторения"], "%d-%m-%Y")
        if date_of_closest_repetition.strftime("%d-%m-%Y") <= datetime.now().strftime("%d-%m-%Y"):
            return 'Ближайшая дата повторения <strong>сегодня</strong>.'
        return f'Ближайшее повторение слов будет <strong> {date_of_closest_repetition.strftime("%d-%m-%Y")}</strong>'
    except IndexError:
        return 'Слов для повторения нет. Начните учить слова, чтобы их повторять.'


def get_profile_message(username: str, list_name: str, chat_id: int) -> str:
    '''получить сообщение профиля'''
    now = datetime.now().strftime("%d-%m-%Y")
    counter = 0
    memorized_words, know_good, know_perfect = calculate_progress(
        list_name, chat_id)
    with open(f"users_data/{chat_id}/explored_words.json", encoding="utf-8") as f:
        list_of_words = json.load(f)
    date_of_closest_repetition = get_date_of_closest_repetition(list_of_words)
    for word in list_name:
        if word["дата повторения"] <= now:
            counter += 1
    return f'''👤 Твой профиль: <strong>{username}</strong>\n\n\
📊 Статистика (в количестве слов):\n• изучил \
<strong>{len(know_good)+len(know_perfect)} из 1194 </strong>\
({round(len(know_perfect)/1194*100)+round(len(know_good)/1194*10, 2)}%) \n\
• начал учить <strong>{len(memorized_words)}</strong>\n\
• знаешь хорошо <strong>{len(know_good)}</strong>\n\
• знаешь отлично <strong>{len(know_perfect)}</strong>\n\n\
📆 Сегодня слов для повторения: <strong>{counter}</strong>.\n\
{date_of_closest_repetition}\n
{get_time_of_reminder(chat_id)}'''


def calculate_progress(list_of_words: list,
                       chat_id: int):
    '''подсчитать прогресс'''
    with open(f"users_data/{chat_id}/explored_words.json", encoding="utf-8") as f:
        list_of_words = json.load(f)
        memorized_words = [
            word for word in list_of_words if word["интервал"] <= 1]
        know_good = [word for word in list_of_words if 2 <=
                     word["интервал"] <= 3]
        know_perfect = [word for word in list_of_words if 4 <=
                        word["интервал"] <= 6]
        return memorized_words, know_good, know_perfect


def format_learning_message(new_word: dict) -> str:
    '''форматировать сообщение об изученном слове'''
    return f'''✍  <em>{new_word['на русском']}</em> → <em>{new_word['на эсперанто']}</em>\n\n\
<strong>Пример предложения:</strong>\n<em>{new_word['пример предложения']}</em>'''


def format_repeating_message(word: dict) -> str:
    '''форматировать сообщение о повторении слова'''
    return f'''❓ Как будет <em>{word['на русском']}</em> на Эсперанто?\n\n\
<strong>Ответ:</strong> <em><tg-spoiler>{word['на эсперанто']}</tg-spoiler></em>\n\n\
<strong>Пример предложения:</strong>\n<em><tg-spoiler>{word['пример предложения']}\
</tg-spoiler></em>'''


def get_time_of_reminder(chat_id):
    '''получить время напоминания'''
    with open('users_data/reminders.json', encoding="utf-8") as f:
        reminders = json.load(f)
        try:
            return f"⏰ Напоминания приходят в <strong>{reminders[str(chat_id)]}</strong> в дни повторений."
        except KeyError:
            return "⏰ Напоминания не установлены."
