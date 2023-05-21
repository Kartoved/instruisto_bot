HELP_COMMAND: str = '''👋 Привет, <em>эсперантист</em>!
Я бот-преподаватель языка <strong>Эсперанто</strong>.
Я помогу тебе выучить этот прекрасный язык!
Ознакомься с моими командами ниже 👇:

<strong>/help</strong> - <em>📋 список команд</em>

Следующие две команды помогут тебе выучить 1202 самых употребительных слова на <em>Эсперанто</em>. Для этого мы с тобой будем учить новые слова и повторять их через увеличивающиеся промежутки времени. За основу метода взята 📈 кривая Эббингауза, но немного модифицированная моим разработчиком. 
<strong>/learning</strong> - <em>🧠 учить новые слова</em>
<strong>/repeating</strong> - <em>🔁 повторять изученные слова</em>
'''

ABOUT_REPEATING: str = '☝️ Сначала ты учишь слова, используя команду <strong>/learning</strong>. Не надо учить сразу все, начни с пяти слов, капля точит камень. Просто читаешь слово и стараешься его запомнить. Будет вдвойне полезно, если ты будешь использовать мнемотехники.\n\nДалее это слово попадает в список для повторения. Слова из этого списка доступны по команде <strong>/repeating</strong>. Слова там будут попадаться через разные промежутки времени: если ты нажимаешь на "✅ помню", то интервал будет увеличиваться. Если на "❌ не помню" — уменьшаться. Минимальный интервал — один день. Максимальный — 24 недели.\n\n🏋️ Старайся заниматься регулярно. Если будешь учить каждый день по 5 слов, то через 241 день будешь знать все 1202 слова из списка, этого хватит для повседневного общения! 😊\n\n🤗 Благодарности:\nСписок слов взят из подборки слов Владимира К. (ник incredibletroth) <a href="https://quizlet.com/incredibletroth/sets">на сайте Quizlet</a>.\nПримеры предложений сконструированы ChatGPT.'

ABOUT_MNEMO: str = '☝️ Мнемотехника, или мнемоника, — это совокупность приёмов, увеличивающих объём памяти и облегчающих запоминание информации, основанная на создании образов и ассоциаций. Мнемотехники можно использовать для запоминания чего угодно.\n🔗 Ниже ссылки, как можно использовать их для запоминания иностранных слов:\n\n<a href="https://youtu.be/-uMqUe55v-M">видео на ютубе</a>\n<a href="https://youtu.be/gh3NCuZHVrg">ещё одно видео</a>\n<a href="https://habr.com/ru/articles/156599/">статья на хабре</a>\n\n☝️ Кроме этих материалов есть и множество других. Изучи вопрос, это крутая тема, которая пригодится тебе во многих сферах жизни!'

CONTACT: str = '🪲 Нашёл баг или ошибку?\n💡 Есть идеи для улучшения?\n😊 Тебе всё нравится, просто хочешь сказать спасибо?\n🖌 Пиши об этом моему разработчику, ссылка ниже 👇'

LEXICON_COMMANDS_RU: dict[str, str] = {
    '/help': '❓ описание бота, список команд',
    '/profile': '📋 профиль',
    '/learning': '📖 учить новые слова',
    '/repeating': '🔁 повторять изученные слова',
    '/contact': '📨 связь с разработчиком'
}

ABOUT_UPDATE: str = f''


def get_profile_message(username: str, list_name: str) -> str:
    return f'''📋 Ваш профиль: <strong>{username}</strong>\n\n📊 Изучено слов {round(len(list_name)/(1202/100), 1)}% ({len(list_name)} из 1202)'''


def format_learning_message(new_word: dict) -> str:
    return f'''📌 <em>{new_word['на русском'].title()}</em> → <em>{new_word['на эсперанто'].upper()}</em>\n\n☝️ Пример предложения: <em>{new_word['пример предложения'].capitalize()}</em>'''


def format_repeating_message(word: dict) -> str:
    return f'''❓ Как будет <em>{word['на русском']}</em> на Эсперанто?\n❗️ Ответ: <em><tg-spoiler>{word['на эсперанто']}</tg-spoiler></em>\n📋 Пример предложения: <em><tg-spoiler>{word['пример предложения']}</tg-spoiler></em>'''
