import random
import qrcode
import os
import gtts
import telebot
from telebot import types

bot = telebot.TeleBot("7103454782:AAFf55hTAtS5jxyOnXXets45o7YvuEkMTeM", parse_mode= None) 

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message , "How can i help you??")
    my_keyboard = types.ReplyKeyboardMarkup(row_width=3)
    
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
@bot.message_handler(func=lambda message: message.text =="Game🎰")
def play_game(message):
    bot.send_message(message.chat.id, "Guess a number between 0 and 50:")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global pc_choice

    my_keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1)
    new_game_key = telebot.types.KeyboardButton("new game")
    my_keyboard.add(new_game_key)

    if message.text.isdigit():
        if int(message.text) > 50:
            bot.send_message(message.chat.id,"Not in the range❌!!!!You have to guess a number between 1 and 50", reply_markup=my_keyboard)
        else:
            if int(message.text) > pc_choice:
                bot.send_message(message.chat.id, "Go Down!!⬇", reply_markup=my_keyboard)
            elif int(message.text) < pc_choice:
                bot.send_message(message.chat.id, "Go Up!!⬆", reply_markup=my_keyboard)
            elif int(message.text) == pc_choice:
                bot.send_message(message.chat.id,"YOU WON!!✅🎉", reply_markup=my_keyboard)

bot.polling()
##################################################################################################### age
@bot.message_handler(commands=['age'])
@bot.message_handler(func=lambda message: message.text =="Age🙋🏻")
def ask_for_birthdate(message):
    bot.send_message(message.chat.id, "Please enter your birthdate in Shamsi format as: (YYYY/MM/DD).")

@bot.message_handler(func=lambda message: "/" in message.text and len(message.text.split("/")) == 3)
def calculate_age(message):
    birthdate = message.text.split("/")
    birthdate = jdate.date(int(birthdate[0]), int(birthdate[1]), int(birthdate[2]))
    today = jdate.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    bot.send_message(message.chat.id, f"You are {age} years old.")
##################################################################################################### voice
@bot.message_handler(commands=['voice'])
@bot.message_handler(func=lambda message: message.text == "Voice🔊")
def ask_for_text(message):
    bot.send_message(message.chat.id, "Please send me a sentence in English to convert to voice, format as:(v: My text).")

@bot.message_handler(func=lambda message: "v:" in message.text)
def text_to_voice(message):
    text_to_convert = message.text.replace('v:', '').strip()
    tts = gTTS(text_to_convert, lang='en')
    voice = io.BytesIO()
    tts.write_to_fp(voice)
    voice.seek(0)
    bot.send_voice(message.chat.id, voice)
#####################################################################################################

bot.infinity_polling() #while loop