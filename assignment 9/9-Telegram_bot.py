import telebot
bot = telebot.TeleBot("7103454782:AAFf55hTAtS5jxyOnXXets45o7YvuEkMTeM", parse_mode= None) 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message , "Welcome to Hasti's bot!!!!🥑")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message , "How can i help you??")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == "Hello":
	    bot.reply_to(message, "Hi!!👸🏻")
    elif message.text == "How are you?":
        bot.reply_to(message, "Im well.")
    elif message.text == "I love you":
        bot.reply_to(message, "💘😇")
    else:
        bot.reply_to(message, "sorry!!I don't understand what you're saying.")




bot.infinity_polling() #while loop