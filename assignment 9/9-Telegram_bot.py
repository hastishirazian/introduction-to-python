import telebot 
import random
import jdatetime
import gtts
from datetime import datetime
import jdatetime as jdate
from telebot import types
from telebot import REPLY_MARKUP_TYPES
from telebot.types import Message
import qrcode

bot = telebot.TeleBot("7103454782:AAFf55hTAtS5jxyOnXXets45o7YvuEkMTeM", parse_mode= None) 

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message , "How can i help you??")
    my_keyboard = types.ReplyKeyboardMarkup(row_width=3)
    
    key1 = types.KeyboardButton('Game🎰')
    key2 = types.KeyboardButton('Age🙋🏻')
    key3 = types.KeyboardButton('Voice🔊')
    key4 = types.KeyboardButton('Max number⏫')
    key5 = types.KeyboardButton('Max index💲')
    key6 = types.KeyboardButton('Qrcode💬')
    key7 = types.KeyboardButton('Help🎀')
    key8 = types.KeyboardButton("Start ✅")

    my_keyboard.add(key8)
    my_keyboard.add(key1, key2 , key3)
    my_keyboard.add(key4, key5, key6)
    my_keyboard.add(key7)
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

    my_keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1)
    new_game_key = telebot.types.KeyboardButton("Game🎰")
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
                bot.stop_polling()

##################################################################################################### age
@bot.message_handler(commands=['age'])
def ask_birthdate(message):
    bot.send_message(message.chat.id, "Please enter your birthdate as this format [year/month/day]:")

@bot.message_handler(func=lambda message: True)
def calculating_age(message):
    today_date = datetime.date.today_date()
    user_birthday = message.text
    user_birthday = user_birthday.split("/")
    today_date = str(today_date)
    today_date = today_date.split("-")
    age_year = int(today_date[0]) - int(user_birthday[0])
    age_month = int(today_date[1]) - int(user_birthday[1])
    age_day = int(today_date[2]) - int(user_birthday[2])
    if today_date[1] < user_birthday[1] :
        age_year -= 1 
        age_month += 12
    if today_date[2] < user_birthday[2] :
        age_day += 30

    output= "Your age is: "+ str(age_year) + " years, " + str(age_month) + " months, and " + str(age_day) + " days."
    bot.send_message(message.chat.id, output)


    my_keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1)
    new_game_key = telebot.types.KeyboardButton("Age🙋🏻")
    my_keyboard.add(new_game_key)

##################################################################################################### voice
@bot.message_handler(commands=['voice'])
def get_text(message):
    ask_for_voice = bot.send_message(message.chat.id, "Enter the English text you want to convert to voice:" )
    
@bot.register_next_step_handler(get_text , text_to_voice)
def text_to_voice(message):
    text = message.text
    voice = gtts.gTTS( text , lang = "en" , slow = False )
    voice.save("Assignment 9/voice1.mp3")
    r_voice = open("Assignment 9/voice1.mp3" ,"rb")
    bot.send_voice(message.chat.id , r_voice)
##################################################################################################### Max number
@bot.message_handler(commands=['max'])
def ask_for_MaxNumber(message):
    bot.send_message(message.chat.id, "Please enter a string of numbers in this format: 13-45-27-11")

@bot.message_handler(func=lambda message: True)
def max_number(message):
    try:
        string = message.text
        array = string.split("-")
        for i in range(len(array)):
            array[i] = int(array[i])
        maximum = array[0]    
        for i in range(1, len(array)):
            if array[i] > maximum:
                maximum = array[i]   
        bot.send_message(message.chat.id, maximum)

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


##################################################################################################### Max index
@bot.message_handler(commands=['index'])
def ask_for_index(message):
    bot.send_message(message.chat.id, "Please enter a string of numbers in this format: 13-45-27-11")

@bot.message_handler(func=lambda message: True)
def max_index(message):
    try:
        string = message.text
        array = string.split("-")
        for i in range(len(array)):
            array[i] = int(array[i])
        maximum = array[0]  
        index = 0 
        for i in range(len(array)):
            if array[i] > maximum:
                maximum = array[i]
                index = i
        argmax = "maximum number is "  + str(maximum) + "\nit's index is : "+ str(index)  
        bot.send_message(message.chat.id , argmax)

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")

##################################################################################################### QRcode
@bot.message_handler(commands=['qrcode'])
def ask_for_text(message):
    bot.send_message(message.chat.id, "Enter Anything to convert it to qrcode :")

@bot.message_handler(func=lambda message: True)
def Qrcode(message):
    q_text = message.text
    qr = qrcode.make(q_text)
    qr.save("Assignment 9/Qrcode1.png")
    qr_image = open("Assignment 9/Qrcode1.png" , "rb")
    bot.send_photo(message.chat.id , qr_image)
#####################################################################################################
bot.infinity_polling() #while loop