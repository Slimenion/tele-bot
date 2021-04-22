import telebot

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
def rules(message):
    id = message.chat.id
    msg = message.text

    if msg == 'Правила' or msg == 'правила' or msg == 'rules' or msg == 'Rules':
        send(id, rules_action)
    else:
        send(id, badAnswer)


bot.polling(none_stop=True)
