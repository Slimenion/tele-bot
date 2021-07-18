import time

import telebot
import parsrer

from config import BOT_TOKEN, admin_id
from phrases import rules_action, badAnswer
from keyboards import keyboard

bot = telebot.TeleBot(BOT_TOKEN)


def send(id, text):
    bot.send_message(id, text, reply_markup=keyboard)


send(admin_id, "Я родился!")


@bot.message_handler(commands=['rules'])
def rules(message):
    send(message.chat.id, 'Тут должны быть правила!')


@bot.message_handler(content_types=['text'])
def quote(message):
    id = message.chat.id
    msg = message.text
    if msg == 'Правила' or msg == 'правила' or msg == 'rules' or msg == 'Rules':
        send(id, rules_action)
    if msg == 'Цитата' or msg == 'цитата':
        send(id, parsrer.parse())


bot.polling(none_stop=True)
