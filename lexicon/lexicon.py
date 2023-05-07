HELP_COMMAND = '''👋 Привет, эсперантист!
Я бот-преподаватель языка <strong>Эсперанто</strong>.
Я помогу тебе выучить этот прекрасный язык, расскажу много интересного и полезного об Эсперанто.
Ознакомься с моими командами ниже 👇:

<strong>/help</strong> - <em>📋 список команд</em>
<strong>/contact</strong> - <em>📱 связаться с разработчиком</em>
<strong>/links</strong> - <em>🔗 полезные ссылки</em>

Следующие две команды помогут тебе выучить 1000 слов на Эсперанто. Для этого мы с тобой будем учить новые слова и повторять их через увеличивающиеся промежутки времени. За основу метода взята 📈 кривая Эббингауза, но немного модифицированная моим разработчиком. 
<strong>/learning</strong> - <em>🧠 учить новые слова</em>
<strong>/repeating</strong> - <em>🔁 повторять изученные слова</em>
'''


LEXICON_COMMANDS_RU: dict[str, str] = {
    '<strong>/help</strong>': '<em>📋 список команд</em>',
    'strong>/contact</strong>': '<em>📱 связаться с разработчиком</em>',
    '<strong>/links</strong>': '<em>🔗 полезные ссылки</em>',
    'strong>/learning</strong>': '<em>🧠 учить новые слова</em>',
    '<strong>/repeating</strong>': '<em>🔁 повторять изученные слова</em>'}

def format_learning_message(new_word: dict):
    return f'''📌 <em>{new_word['на русском'].title()}</em> ➡️ <em>{new_word['на эсперанто'].upper()}</em>\n☝️ Пример предложения: <em>{new_word['пример предложения'].capitalize()}</em>'''


def format_repeating_message(word: dict):
    return f'''❓Как будет <em>{word['на русском']}</em> на Эсперанто?\n➡️ Ответ: <em><tg-spoiler>{word['на эсперанто']}</tg-spoiler></em>\n☝️ Пример предложения: <em><tg-spoiler>{word['пример предложения']}</tg-spoiler></em>'''
