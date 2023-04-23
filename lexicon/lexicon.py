HELP_COMMAND = '''Привет, эсперантист!
Я бот-преподаватель языка <strong>Эсперанто</strong>.
Я помогу тебе выучить этот прекрасный язык, расскажу много интересного и полезного об Эсперанто.
Ознакомься с моими командами ниже:

<strong>/help</strong> - <em>список команд</em>
<strong>/start</strong> - <em>запустить бота</em>
<strong>/contact</strong> - <em>связаться с разработчиком</em>
<strong>/links</strong> - <em>полезные ссылки</em>
<strong>/learning</strong> - <em>учить новые слова</em>
<strong>/training</strong> - <em>запоминать изученные слова</em>
'''


LEXICON_RU = {
}


def format_learning_message(new_word: dict):
    return f'''📌 <em>{new_word['на русском'].title()}</em> ➡️ <em>{new_word['на эсперанто'].upper()}</em>\n☝️ Пример предложения: <em>{new_word['пример предложения'].capitalize()}</em>'''


def format_training_message(word: dict):
    return f'''❓Как будет <em>{word['на русском']}</em> на Эсперанто?\n➡️ Ответ: <em><tg-spoiler>{word['на эсперанто']}</tg-spoiler></em>\n☝️ Пример предложения: <em><tg-spoiler>{word['пример предложения']}</tg-spoiler></em>'''
