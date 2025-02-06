import telebot
from settings import TOKEN

bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.username}! Напиши название страны, и я скажу её столицу.")

@bot.message_handler(content_types=['text'])
def handle_country_name(message):
    country = message.text.lower().strip()
    capital = capitals.get(country)
    if capital:
        bot.reply_to(message, f"Столица {country} — {capital}.")
    else:
        bot.reply_to(message, "Извини, я не знаю столицу этой страны.")

bot.polling()
