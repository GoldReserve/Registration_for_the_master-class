import telebot

import telebot

#Токен желательно брать из другого файла, а не прописывать здесь
bot = telebot.TeleBot('')

# В идеале не хардкодить id
user_id = 456064521

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")
    # Отсюда дальше можно chat_id вытаскивать, но поскольку у нас один единственный человек которому бот отправляет то надобности нет

def send_message(data: dict = None):
    message = f"<b>{data['name']}</b> записался на мастер класс <i>№{data['master_class']}</i> на " \
              f"<b>{data['date']}</b>. \n<i>Почта:</i> <b>{data['email']}</b>" \
              f"<i>Телефон:</i> <b>{data['number']}</b>"
    bot.send_message(user_id, message, parse_mode='html')


