import sqlite3 as sq
import telebot
from telebot import types
db = sq.connect('bot.db', check_same_thread=False)
cur = db.cursor()

#cur.execute("SELECT answers FROM repl WHERE questions = '{}'".format(input()))
#res = cur.fetchone()

bot = telebot.TeleBot("1439430835:AAET1HHSIaK68uQmQpVcDAqauoc8-UlPBrs")


@bot.message_handler(content_types=['text'])
def text_answers(message):
    try:
        cur.execute("SELECT answers FROM repl WHERE questions = '{}'".format(message.text.lower()))
        res = cur.fetchone()
        bot.send_message(message.from_user.id, *res)
        if res == ('Пофотодрочим? ',):
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text='Да', callback_data='yes'))
            keyboard.add(types.InlineKeyboardButton(text='Нет', callback_data='no'))
            bot.send_message(message.from_user.id, text="A?", reply_markup=keyboard)
    except TypeError:
        bot.send_message(message.from_user.id, "Не понимаю тебя(\nПопробуй /Help")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Сначала купи микрат)')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Зря')


bot.polling()

