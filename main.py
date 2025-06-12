import telebot

API_KEY = '7570268725:AAEBUb1Fu42mHIe9K6wgn6nrQJScMzInoyo'
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Welcome to GHSMMSTORE DIGITAL HUB!")

bot.polling()
