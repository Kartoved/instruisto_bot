"""различный текст для бота"""

from datetime import datetime
import json


LINKS: str = """🔗 Полезные ссылки:
— <a href="https://t.me/babilejo_eo_ru">Чат эсперантистов в телеграм</a> 
— <a href="https://vk.com/priesperanto">Паблик Эсперанто ВК</a> 
— <a href="https://vk.com/por_pigruloj">Паблик ВК "Эсперанто для лентяев"</a> 
— <a href="https://lernu.net/">Многоязычный сайт для изучения международного языка эсперанто</a> 
— <a href="https://kurso.com.br/index.php?ru">Курс обучения Эсперанто. Приложение для Android, Windows, Mac, Linux</a> 

Список будет пополняться. 
"""

HELP_COMMAND: str = """👋 Привет, начинающий <em>эсперантист</em>!
Я бот-преподаватель языка <strong>Эсперанто</strong>.
Я помогу тебе выучить этот прекрасный язык!
Ознакомься с моими командами ниже 👇:

<strong>/help</strong> — <em>🗒 список команд</em>
<strong>/profile</strong> — <em>📋 профиль</em>
<strong>/contact</strong> — <em>📨 связь с разработчиком</em>
<strong>/links</strong> — <em>🔗 полезные ссылки на материалы, где ты сможешь глубже изучить Эсперанто</em>

Следующие две команды помогут тебе выучить 1194 самых употребительных слова \
на <em>Эсперанто</em>. Для этого мы с тобой будем учить новые слова \
и повторять их через увеличивающиеся промежутки времени. \
За основу метода взята 📈 кривая Эббингауза, но немного модифицированная \
моим разработчиком. 
<strong>/learning</strong> - <em>🧠 учить новые слова</em>
<strong>/repeating</strong> - <em>🔁 повторять изученные слова</em>

Также эти кнопки доступны в <em>меню бота</em> и в <em>профиле</em>.
"""

ABOUT_REPEATING: str = '☝️ Сначала ты учишь слова, используя команду \
<strong>/learning</strong>. Не надо учить сразу все, начни с пяти слов, \
капля точит камень. Просто читаешь слово и стараешься его запомнить. \
Будет вдвойне полезно, если ты будешь использовать мнемотехники.\n\n\
Далее это слово попадает в список для повторения. Слова из этого списка \
доступны по команде <strong>/repeating</strong>. Слова там будут попадаться \
через разные промежутки времени: если ты нажимаешь на "✅ помню", \
то интервал будет увеличиваться. Если на "❌ не помню" — уменьшаться. \
Минимальный интервал — один день. Максимальный — 24 недели.\n\n\
🏋️ Старайся заниматься регулярно. Если каждый день учить по 5 слов,\
то через 239 дней будешь знать все 1194 слова из списка! \
Этого хватит для базового повседневного общения. 😊\n\n\
Разработчик: <a href="https://t.me/prepod_wood">Вуд Романов</a>\n\n\
🤗 Благодарности:\n— Список слов взят из подборки слов Владимира К. \
(ник incredibletroth) <a href="https://quizlet.com/incredibletroth/sets">на сайте Quizlet</a>.\n— Примеры предложений сконструированы ChatGPT.\n — Корректировщики-эсперантисты: <a href="https://vk.com/sskumkov">Сергей Кумков</a> , <a href="https://t.me/legado_eo_ru">Tatjana</a>, Aleksei Samsonov\n — Аватарка бота сгенерирована Midjourney\n — Спасибо всем, кто участвовал в тестировании!'

ABOUT_MNEMO: str = '☝️ Мнемотехника, или мнемоника, — это совокупность \
приёмов, увеличивающих объём памяти и облегчающих запоминание информации, \
основанная на создании образов и ассоциаций. Мнемотехники можно использовать \
для запоминания чего угодно.\n🔗 Ниже ссылки, как можно использовать их \
для запоминания иностранных слов:\n\n<a href="https://youtu.be/-uMqUe55v-M">\
— видео на ютубе</a>\n<a href="https://youtu.be/gh3NCuZHVrg">— ещё одно видео</a> \
\n<a href="https://habr.com/ru/articles/156599/">— статья на хабре</a>\n\n\
☝️ Кроме этих материалов есть и множество других. Изучи вопрос, \
это крутая тема, которая пригодится тебе во многих сферах жизни!'

CONTACT: str = '🪲 Нашёл баг или ошибку?\n💡 Есть идеи для улучшения?\n\
😊 Тебе всё нравится, просто хочешь сказать спасибо?\
\n🖌 Напиши об этом моему разработчику ответным сообщением в этом чате. \
Если передумал, то нажми <em>"отмена"</em>'

LEXICON_COMMANDS_RU: dict[str, str] = {
    "/help": "❓ описание бота, список команд",
    "/profile": "📋 профил"',
    "/learning": "📖 учить новые слов"',
    "/repeating": "🔁 повторять изученные слов"',
    "/links": "🔗 полезные ссылк"',
    "/contact": "📨 связь с разработчико"',
}

ABOUT_UPDATE: str = f""


RESET_MESSAGE: str = "‼️‼️‼️ Вы уверены, что хотите сбросить прогресс? ‼️‼️‼️\
\n\nЭто действие НЕОБРАТИМО! Сбросится статистика, удалятся все изученные\
 слова и придётся учить их заново!"


def get_profile_message(username: str, list_name: str) -> str:
    now = datetime.now().strftime("%d-%m-%Y")
    counter = 0
    memorized_words, know_good, know_perfect = calculate_progress(list_name)
    for word in list_name:
        if word["дата повторения"] <= now:
            counter += 1
    return f"""📋 Ваш профиль: <strong>{username}</strong>\n\n\
📊 Статистика:\n— изучено слов: \
<strong>{round(len(know_perfect)/1194*100)+round(len(know_good)/1194*10, 2)}%</strong> \
({len(know_good)+len(know_perfect)} из 1194 слов)\n\
— начал учить <strong>{len(memorized_words)}</strong> слов(о/а).\n\
— знаешь хорошо <strong>{len(know_good)}</strong> слов(о/а).\n\
— знаешь отлично <strong>{len(know_perfect)}</strong> слов(о/а).\n\n\
📆 Сегодня слов для повторения: <strong>{counter}</strong"""'


def calculate_progress(list_of_words: list):
    with open("users_data/164720191/explored_words.json", encoding="utf-8") as f:
        list_of_words: list = json.load(f)
        memorized_words = []
        know_good = []
        know_perfect = []
        for word in list_of_words:
            if word["интервал"] <= 1:
                memorized_words.append(word)
            elif word["интервал"] <= 3:
                know_good.append(word)
            elif word["интервал"] <= 6:
                know_perfect.append(word)
        return memorized_words, know_good, know_perfect


def format_learning_message(new_word: dict) -> str:
    return f"""✍ <em>{new_word['на русском'].upper()}</em> → <em>{new_word['на эсперанто'].upper()}</em>\n\n☝️ Пример предложения: <em>{new_word['пример предложения']}</em>"""


def format_repeating_message(word: dict) -> str:
    return f"""❓ Как будет <em>{word['на русском']}</em> на Эсперанто?\n❗️ \
Ответ: <em><tg-spoiler>{word['на эсперанто']}</tg-spoiler></em>\n\
📋 Пример предложения: <em><tg-spoiler>{word['пример предложения']}\
</tg-spoiler></em>"""
