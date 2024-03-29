import random
import qrcode
import telebot
from telebot import types

bot = telebot.TeleBot("7103454782:AAFf55hTAtS5jxyOnXXets45o7YvuEkMTeM", parse_mode= None) 

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message , "How can i help you??")
    my_keyboard = types.ReplyKeyboardmy_keyboard(row_width=3)
    
    key1 = types.KeyboardButton('Game🎰')
    key2 = types.KeyboardButton('Age🙋🏻')
    key3 = types.KeyboardButton('Voice🔊')
    key4 = types.KeyboardButton('Max number⏫')
    key5 = types.KeyboardButton('Argmax💲')
    key6 = types.KeyboardButton('Qrcode💬')
    key7 = types.KeyboardButton('Help🎀')
    key8 = types.KeyboardButton("Start ✅")

    my_keyboard.row(key8)
    my_keyboard.row(key1, key2 , key3)
    my_keyboard.row(key4, key5, key6)
    my_keyboard.row(key7)
    bot.send_message(message.chat.id ,"Choose one of the below keys :" , reply_markup=my_keyboard)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello {}! Welcome to Hasti's bot!!!!🥑".format(message.from_user.first_name))

##################################################################################################### game
pc_choice = random.randint(1,50)
@bot.message_handler(commands=['game'])
def play_game(message):
    bot.send_message(message.chat.id, "Guess a number between 0 and 50:")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global pc_choice

    new_keyboard= telebot.types.ReplyKeyboardMarkup(row_width=1)
    new_game_key = telebot.types.KeyboardButton("new game")
    new_keyboard.add(new_game_key)

    if int(message.text) > pc_choice:
	    bot.send_message(message.chat.id, "Go Down!!⬇", reply_markup=new_keyboard)
    elif int(message.text) < pc_choice:
        bot.send_message(message.chat.id, "Go Up!!⬆", reply_markup=new_keyboard)
    elif int(message.text) == pc_choice:
        bot.send_message(message.chat.id,"YOU WON!!✅🎉", reply_markup=new_keyboard)
bot.polling()
#####################################################################################################

bot.infinity_polling() #while loop