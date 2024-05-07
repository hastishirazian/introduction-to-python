import telebot 
import random
import gtts
from datetime import datetime
from telebot import types
from telebot import REPLY_MARKUP_TYPES
from telebot.types import Message
import qrcode
from persiantools.jdatetime import JalaliDate


bot = telebot.TeleBot("7103454782:AAFf55hTAtS5jxyOnXXets45o7YvuEkMTeM", parse_mode= None) 

my_keyboard = types.ReplyKeyboardMarkup(row_width=3)

key1 = types.KeyboardButton('Game🎰')
key2 = types.KeyboardButton('Age🙋🏻')
key3 = types.KeyboardButton('Voice🔊')
key4 = types.KeyboardButton('Max number⏫')
key5 = types.KeyboardButton('Max index💲')
key6 = types.KeyboardButton('Qrcode💬')
key7 = types.KeyboardButton('Help🎀')

my_keyboard.add(key1, key2 , key3)
my_keyboard.add(key4, key5, key6)
my_keyboard.add(key7)
##################################################################################################### send welcome & menu
bot.send_message(message.chat.id ,"Choose one of the below keys :" , reply_markup=my_keyboard)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello {}! Welcome to Hasti's bot!!!!🥑".format(message.from_user.first_name), reply_markup=my_keyboard)

@bot.message_handler(commands=['help'])
@bot.message_handler(func=lambda message: message.text == "Help🎀")

def help(message):
    bot.reply_to(message , "How can i help you??")

    help_text += "/start : Welcome.\n"
    help_text += "/game : Guess number game.\n"
    help_text += "/age : Calculate your age.\n"
    help_text += "/voice : Convert a text to audio file.\n"
    help_text += "/max : Find the maximum number.\n"
    help_text += "/argmax : Find the index of the max number.\n"
    help_text += "/qrcode : Make a QR code from the input text."
    bot.reply_to ( message , help_text )

# # ##################################################################################################### game
@bot.message_handler(commands=['game'])
@bot.message_handler(func=lambda message: message.text == "Game🎰")
def ask_random_number(message):
    global pc_choice
    pc_choice = random.randint(1,50)

    bot.send_message(message.chat.id, "Guess a number between 0 and 50:")

@bot.message_handler(func=lambda message: True ) 
def guess_number(message1):

    if message1.text.isdigit():
        if int(message1.text) > 50:
            bot.send_message(message1.chat.id,"Not in the range❌!!!!You have to guess a number between 1 and 50", reply_markup=my_keyboard)
        else:
            if int(message1.text) > pc_choice:
                bot.send_message(message1.chat.id, "Go Down!!⬇")
            elif int(message1.text) < pc_choice:
                bot.send_message(message1.chat.id, "Go Up!!⬆")
            elif int(message1.text) == pc_choice:
                bot.send_message(message1.chat.id,"YOU WON!!✅🎉")
# ##################################################################################################### age
@bot.message_handler(commands=['age'])
@bot.message_handler(func=lambda message: message.text == "Age🙋🏻")
def ask_birthdate(message):
    bot.send_message(message.chat.id, "Please enter your birthdate as this format [year/month/day]:")


@bot.message_handler(func=lambda message: True)
def calculating_age(message):

    today_date = JalaliDate.today()

    user_birthday = message.text.split("/")
    birth_year, birth_month, birth_day = map(int, user_birthday)

    age_year = today_date.year - birth_year
    age_month = today_date.month - birth_month
    age_day = today_date.day - birth_day

    if today_date.month < birth_month or (today_date.month == birth_month and today_date.day < birth_day):
        age_year -= 1
        age_month = 12 - birth_month + today_date.month
        if today_date.day < birth_day:
            age_month -= 1
            age_day = today_date.day + (30 - birth_day)
    
    output = "Your age is: " + str(age_year) + " years, " + str(age_month) + " months, and " + str(age_day) + " days."
    bot.send_message(message.chat.id, output)
######################################################################################################### voice
@bot.message_handler(commands=['voice'])
@bot.message_handler(func=lambda message: message.text == "Voice🔊")
def ask_text(message):
    bot.send_message(message.chat.id, "Enter the English text you want to convert to voice:" )
    
    @bot.message_handler(func=lambda message: True)
    def text_to_voice(message):

        text = message.text
        voice = gtts.gTTS( text , lang = "en" , slow = False )
        voice.save("C:/Users/rcc2/Desktop/hasti git/introduction-to-python/assignment 9/voice1.mp3")
        r_voice = open("C:/Users/rcc2/Desktop/hasti git/introduction-to-python/assignment 9/voice1.mp3" ,"rb")
        bot.send_voice(message.chat.id , r_voice)
######################################################################################################### Max number
@bot.message_handler(commands=['max'])
@bot.message_handler(func=lambda message: message.text == "Max number⏫")
def ask_MaxNumber(message):
    bot.send_message(message.chat.id, "Please enter a string of numbers in this format: 13-45-27-11")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def max_number(message):

    string = message.text
    array = string.split("-")
    for i in range(len(array)):
        array[i] = int(array[i])
    maximum = array[0]    
    for i in range(1, len(array)):
        if array[i] > maximum:
            maximum = array[i]   
    bot.send_message(message.chat.id, maximum)
##################################################################################################### Max index
@bot.message_handler(commands=['index'])
@bot.message_handler(func=lambda message: message.text == "Max index💲")
def ask_index(message):
    bot.send_message(message.chat.id, "Please enter a string of numbers in this format: 13-45-27-11")

@bot.message_handler(func=lambda message: True)
def max_index(message):

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
##################################################################################################### QRcode
@bot.message_handler(commands=['qrcode'])
@bot.message_handler(func=lambda message: message.text == "Qrcode💬")
def ask_for_text(message):
    bot.send_message(message.chat.id, "Enter Anything to convert it to qrcode :")

    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def Qrcode(message):

        q_text = message.text
        qr = qrcode.make(q_text)
        qr.save("C:/Users/rcc2/Desktop/hasti git/introduction-to-python/assignment 9/Qrcode1.png")
        qr_image = open("C:/Users/rcc2/Desktop/hasti git/introduction-to-python/assignment 9/Qrcode1.png", "rb")
        bot.send_photo(message.chat.id, qr_image)

#######################################################################################################

bot.infinity_polling() #while loop
