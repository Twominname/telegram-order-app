import telebot
from telebot import types

TOKEN = 'ваш_токен_бота'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем кнопку для запуска Web App
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item = types.KeyboardButton("Заказать", web_app=types.WebAppInfo(url="https://your-web-app-url.com"))
    markup.add(item)

    bot.send_message(message.chat.id, "Привет! Я твой заказной бот. Нажми кнопку для начала.", reply_markup=markup)

bot.polling()
