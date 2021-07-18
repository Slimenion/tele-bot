import telebot


keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Правила', 'Акции')
keyboard.row('Цитата')