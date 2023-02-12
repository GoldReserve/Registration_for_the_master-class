import telebot

import telebot

token = 'наш токен'
bot = telebot.TeleBot('5992992573:AAGQdyN371hgktZwfcS5qUUVGPbNPJwYWfo')


@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.chat.id
    bot.send_message(message.chat.id, "Привет ✌️ ")
    send_message('Ку ку')


def send_message(message=None, data: dict = None):
    bot.send_message(user_id, f'{message}')


bot.infinity_polling()
