import telebot
from telebot import types

TOKEN = '7926473843:AAERqSOZ2U2hGPWPQIA6oSUl4kwQjpF1_vU'  # Замените на токен вашего бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Создаем инлайн кнопку с переходом на мини-приложение
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(
        text="Перейти к меню", 
        web_app=types.WebAppInfo(url="https://twominname.github.io/telegram-order-app/index.html")  # Замените на свой URL
    )
    markup.add(button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы открыть меню и сделать заказ.", reply_markup=markup)

# Обработчик всех сообщений (если нужно)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Если ты хочешь сделать заказ, нажми на кнопку ниже.")

# Запуск бота
bot.polling(none_stop=True)
