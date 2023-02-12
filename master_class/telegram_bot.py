import telebot

import telebot

token = 'наш токен'
bot = telebot.TeleBot('5992992573:AAGQdyN371hgktZwfcS5qUUVGPbNPJwYWfo')
user_id = 456064521

@bot.message_handler(commands=['start'])
def start_message(message):
    # global
    # user_id = message.chat.id
    bot.send_message(message.chat.id, "Привет ✌️ ")
    send_message('Ку ку')


def send_message(data: dict = None):
    message = f"<b>{data['name']}</b> записался на мастер класс <i>№{data['master_class']}</i> на " \
              f"<b>{data['date']}</b>. \n<i>Почта:</i> <b>{data['email']}</b>" \
              f"<i>Телефон:</i> <b>{data['number']}</b>"
    bot.send_message(user_id, message, parse_mode='html')



# bot.infinity_polling()
